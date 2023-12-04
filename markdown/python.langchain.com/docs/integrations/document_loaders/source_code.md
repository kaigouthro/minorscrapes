

Skip to main content

On this page

# Source Code

This notebook covers how to load source code files using a special approach with language parsing: each top-level function and class in the code is loaded into separate documents. Any remaining code
top-level code outside the already loaded functions and classes will be loaded into a separate document.

This approach can potentially improve the accuracy of QA models over source code. Currently, the supported languages for code parsing are Python and JavaScript. The language used for parsing can be
configured, along with the minimum number of lines required to activate the splitting based on syntax.

```python




    pip install esprima



```


```python




    import warnings

    warnings.filterwarnings("ignore")
    from pprint import pprint

    from langchain.document_loaders.generic import GenericLoader
    from langchain.document_loaders.parsers import LanguageParser
    from langchain.text_splitter import Language



```


```python




    loader = GenericLoader.from_filesystem(
        "./example_data/source_code",
        glob="*",
        suffixes=[".py", ".js"],
        parser=LanguageParser(),
    )
    docs = loader.load()



```


```python




    len(docs)



```


```python




        6



```


```python




    for document in docs:
        pprint(document.metadata)



```


```python




        {'content_type': 'functions_classes',
         'language': <Language.PYTHON: 'python'>,
         'source': 'example_data/source_code/example.py'}
        {'content_type': 'functions_classes',
         'language': <Language.PYTHON: 'python'>,
         'source': 'example_data/source_code/example.py'}
        {'content_type': 'simplified_code',
         'language': <Language.PYTHON: 'python'>,
         'source': 'example_data/source_code/example.py'}
        {'content_type': 'functions_classes',
         'language': <Language.JS: 'js'>,
         'source': 'example_data/source_code/example.js'}
        {'content_type': 'functions_classes',
         'language': <Language.JS: 'js'>,
         'source': 'example_data/source_code/example.js'}
        {'content_type': 'simplified_code',
         'language': <Language.JS: 'js'>,
         'source': 'example_data/source_code/example.js'}



```


```python




    print("\n\n--8<--\n\n".join([document.page_content for document in docs]))



```


```python




        class MyClass:
            def __init__(self, name):
                self.name = name

            def greet(self):
                print(f"Hello, {self.name}!")

        --8<--

        def main():
            name = input("Enter your name: ")
            obj = MyClass(name)
            obj.greet()

        --8<--

        # Code for: class MyClass:


        # Code for: def main():


        if __name__ == "__main__":
            main()

        --8<--

        class MyClass {
          constructor(name) {
            this.name = name;
          }

          greet() {
            console.log(`Hello, ${this.name}!`);
          }
        }

        --8<--

        function main() {
          const name = prompt("Enter your name:");
          const obj = new MyClass(name);
          obj.greet();
        }

        --8<--

        // Code for: class MyClass {

        // Code for: function main() {

        main();



```


The parser can be disabled for small files.

The parameter `parser_threshold` indicates the minimum number of lines that the source code file must have to be segmented using the parser.

```python




    loader = GenericLoader.from_filesystem(
        "./example_data/source_code",
        glob="*",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=1000),
    )
    docs = loader.load()



```


```python




    len(docs)



```


```python




        1



```


```python




    print(docs[0].page_content)



```


```python




        class MyClass:
            def __init__(self, name):
                self.name = name

            def greet(self):
                print(f"Hello, {self.name}!")


        def main():
            name = input("Enter your name: ")
            obj = MyClass(name)
            obj.greet()


        if __name__ == "__main__":
            main()




```


## Splitting​

Additional splitting could be needed for those functions, classes, or scripts that are too big.

```python




    loader = GenericLoader.from_filesystem(
        "./example_data/source_code",
        glob="*",
        suffixes=[".js"],
        parser=LanguageParser(language=Language.JS),
    )
    docs = loader.load()



```


```python




    from langchain.text_splitter import (
        Language,
        RecursiveCharacterTextSplitter,
    )



```


```python




    js_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.JS, chunk_size=60, chunk_overlap=0
    )



```


```python




    result = js_splitter.split_documents(docs)



```


```python




    len(result)



```


```python




        7



```


```python




    print("\n\n--8<--\n\n".join([document.page_content for document in result]))



```


```python




        class MyClass {
          constructor(name) {
            this.name = name;

        --8<--

        }

        --8<--

        greet() {
            console.log(`Hello, ${this.name}!`);
          }
        }

        --8<--

        function main() {
          const name = prompt("Enter your name:");

        --8<--

        const obj = new MyClass(name);
          obj.greet();
        }

        --8<--

        // Code for: class MyClass {

        // Code for: function main() {

        --8<--

        main();



```
