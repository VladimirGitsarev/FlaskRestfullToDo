# Api Overview

Get a list of all items
### Request

`GET items/`

Get one particular item
### Request

`GET items/<id>`

Create new item
### Request

`POST items/`

    {
        "name": "New",
        "description": "Again"
    }
### Response

    {
        "description": "Again",
        "id": 1,
        "name": "New",
        "date": "2021-10-04T18:11:51.935145",
        "done": false
    }

Update item
### Request

`PATCH items/<id>`

    {
        "name": "New Update",
        "description": "Again Update",
        "done": true
    }
### Response

    {
        "description": "Again Update",
        "id": 1,
        "name": "New Update",
        "date": "2021-10-04T18:11:51.935145",
        "done": true
    }