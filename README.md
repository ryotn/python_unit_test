# Python テスト＆カバレッジ サンプルプロジェクト

このリポジトリは、Pythonプログラムのユニットテストとカバレッジ測定を行うためのシンプルなサンプルプロジェクトです。

## プロジェクト構成

```text
.
├── program/
│   ├── main.py       # サンプルの関数群 (add_one, multiply_by_two, my_partial_fn)
│   └── main2.py      # サンプルの関数群 (add_three)
├── tests/
│   ├── __init__.py
│   └── test_main.py  # program/main.py に対するユニットテスト
├── README.md         # このファイル
├── requirements.txt  # 依存関係 (coverage>=6.5)
├── run_coverage.py   # テストの実行とカバレッジレポート生成スクリプト
└── LICENSE           # MIT License
```

## セットアップ

このプロジェクトではカバレッジ測定に `coverage` パッケージを使用しています。以下のコマンドで依存パッケージをインストールしてください。

```bash
pip install -r requirements.txt
```

## テストとカバレッジの実行

プロジェクト内のすべてのテストを実行し、カバレッジを測定するには `run_coverage.py` を実行します。

```bash
python run_coverage.py
```

このスクリプトを実行すると、以下の処理が自動で行われます。
1. `coverage` モジュールが未インストールの場合は自動的にインストール
2. `unittest` を使用して `test*.py` に一致するテストを実行
3. ターミナルにカバレッジレポートを出力
4. `htmlcov/` ディレクトリにHTML形式のカバレッジレポートを生成

生成されたHTMLレポートは、ブラウザで `htmlcov/index.html` を開くことで詳細を確認できます。

## ライセンス

このプロジェクトは MIT License のもとで公開されています。詳細は [LICENSE](LICENSE) ファイルをご確認ください。
