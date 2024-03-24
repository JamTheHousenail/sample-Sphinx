# memo

## pygments_style

コードブロックのスタイルを変更

[一覧はこちら](https://pygments.org/styles/)

```text
pygments_style = "lightbulb"
```

## テスト

```{code-block} vb.net
:force:
dim test as new test

' コメントはどうなるのか
private sub testSub()
    dim test as new test
    return ${test.tostring}
end sub
```

```{code-block} sql
SELECT *
  FROM user_tab_columns
```

```{code-block} text
:caption: sphinx auto-build
sphinx-autobuild ./source ./build/html 
```

```{code-block} text
sphinx-autobuild ./source ./build/html 
```

```{todo}
TODO:ここに配置
```

## sphinx.ext.todo

### 準備

インストール不要

conf.py に以下の設定を追記

```text
extensions = [
    'sphinx.ext.todo',
]

todo_include_todos = True
```

```{note}
todo_include_todos をFalse に設定すると出力されない
```

### TODOの書き方

コードブロックでTODOを書く

````text
```{todo}
TODOの書き方
```
````

### TODOを出力する

コードブロックでtodolistを指定すると一覧で出力される

````text
```{todolist}
```
````
