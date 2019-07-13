# coding=utf-8
"""シンプルなパイプライン."""

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, GoogleCloudOptions


class MyOptions(PipelineOptions):
    """パラメータを受け取るためのカスタムオプションクラス."""

    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--input',
            default='gs://dataflow-reference/source/input.txt',
            help='Input gcs file path.')

        parser.add_argument(
            '--output',
            default='gs://dataflow-reference/sink/output.txt',
            help='Output gcs file path.')

        parser.add_value_provider_argument(
            '--suffix',
            default='!',
            help='Output gcs file path.')


class MyReplaceFn(beam.DoFn):
    def __init__(self, vp_suffix):
        self._vp_suffix = vp_suffix

    def process(self, element):
        yield element.replace('.', self._vp_suffix.get())


if __name__ == '__main__':
    options = MyOptions()

    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = 'dataflow-reference'  # プロジェクトID
    google_cloud_options.job_name = 'myjob'  # 任意のジョブ名
    google_cloud_options.staging_location = 'gs://dataflow-reference/binaries'  # 作成したバケット以下の任意のロケーション
    google_cloud_options.temp_location = 'gs://dataflow-reference/tmp'  # 作成したバケット以下の任意のロケーション
    google_cloud_options.template_location = 'gs://dataflow-reference/template'  # テンプレートのファイルを保存する場所を指定する
    options.view_as(StandardOptions).runner = 'DataflowRunner'  # ランナーには「DataflowRunner」を指定

    p = beam.Pipeline(options=options)

    (p
     | 'ReadFromText' >> beam.io.ReadFromText(options.input)  # オプションで指定したパスのファイルを読み取る
     | 'ReplaceSuffix' >> beam.ParDo(MyReplaceFn(options.suffix))  # 接尾辞を「.」から指定したものに入れ替える
     | 'WriteToText' >> beam.io.WriteToText(options.output))  # オプションで指定したパスにファイルを書き込む

    p.run()
