# Research: JSON

## 1. What does JSON stand for?

JSON stands for **JavaScript Object Notation**. It is a lightweight format used to store and exchange data.

## 2. What is JSON used for?

JSON is used to store and transfer data between applications and systems.

For example:
- Sending data between a website and a server.
- Storing information about books, users or products.
- Working with APIs.
- Transferring data between different programming languages.

## 3. What is JSON written in?

JSON is a text-based format. Its syntax is based on JavaScript object notation, but JSON is language-independent, meaning it can be used with languages such as Python, Java, JavaScript and C#.

JSON files usually use the `.json` file extension.

## 4. Advantages of using JSON

- **Easy to read:** The structure is clear and human-readable.
- **Lightweight:** It does not require much extra formatting.
- **Language-independent:** Many programming languages can work with JSON.
- **Easy to exchange:** It is commonly used when transferring data between applications.
- **Supports structured data:** Objects and arrays can be used to organise information.
- **Works with APIs:** Many APIs use JSON to send and receive data.

## 5. What data types can JSON store?

JSON supports six types of values:

| Data type | Description | Example |
|---|---|---|
| String | Text surrounded by double quotation marks | `"Salma"` |
| Number | An integer or decimal number | `25` or `4.5` |
| Boolean | A true or false value | `true` |
| Null | Represents an empty or missing value | `null` |
| Object | A collection of name and value pairs | `{"name": "Salma"}` |
| Array | An ordered list of values | `["Python", "SQL"]` |

JSON does not have a separate data type for dates. Dates are commonly stored as strings.

## 6. JSON syntax

### Name and value pairs

A name and value pair contains a key and its value. The key must be a string written in double quotation marks, followed by a colon and the value.

```json
"name": "Salma",
```

Here, `name` is the key and `Salma` is the value.

### Objects

An object is a collection of name and value pairs enclosed in curly brackets `{}`.

```json
{
    "name": "Salma",
    "age": 23,
    "course": "Data Academy"
}
```

Each pair contains a key and a value. An object can contain different data types.

### Separating name and value pairs

A colon `:` separates a key from its value.

A comma `,` separates one pair from another.

```json
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
```

In this example, the colon separates each key from its value, while the commas separate the pairs.

Do not add a trailing comma after the final pair.

### JSON arrays

An array is an ordered list of values enclosed in square brackets `[]`. The values are separated by commas.

```json
{
    "genres": [
        "Romance",
        "Fantasy",
        "Mystery"
    ]
}
```

Arrays can contain strings, numbers, booleans, objects and other arrays.

## Summary

JSON stands for JavaScript Object Notation. It is a lightweight, text-based format used to store and exchange structured data. Its main syntax includes objects `{}`, arrays `[]`, colons `:` and commas `,`. JSON is widely used in APIs and applications because it is readable, easy to transfer and supported by many programming languages.