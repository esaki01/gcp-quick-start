"""シンプルなパイプライン."""

# coding=utf-8
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


if __name__ == '__main__':
    options = MyOptions()

    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = 'dataflow-reference'  # プロジェクトID
    google_cloud_options.job_name = 'myjob'  # 任意のジョブ名
    google_cloud_options.staging_location = 'gs://dataflow-reference/binaries'  # 作成したバケット以下の任意のロケーション
    google_cloud_options.temp_location = 'gs://dataflow-reference/tmp'  # 作成したバケット以下の任意のロケーション
    options.view_as(StandardOptions).runner = 'DataflowRunner'  # ランナーには「DataflowRunner」を指定

    p = beam.Pipeline(options=options)

    (p
     | 'ReadFromText' >> beam.io.ReadFromText(options.input)  # オプションで指定したパスのファイルを読み取る
     | 'ComputeWordLength' >> beam.Map(lambda element: len(element))  # 1行ごとに文字数を数える
     | 'WriteToText' >> beam.io.WriteToText(options.output))  # オプションで指定したパスにファイルを書き込む

    p.run()
