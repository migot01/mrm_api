null = None

create_block_query = '''
  mutation{
  createBlock(officeId:2, name:"blask" ) {
    block{
      officeId
        name
      }
  }
}
'''

create_block_response = {
  "data": {
    "createBlock": {
      "block": {
        "officeId": 2,
        "name": "Blask"
      }
    }
  }
}

block_mutation_query_without_name = '''
     mutation{
    createBlock(officeId:2, name:"" ) {
        block{
            officeId
            name
        }
    }
}
'''

block_creation_with_duplicate_name = '''
mutation{
  createBlock(officeId:2 name:"Ec" ) {
    block{
      officeId
        name
      }
  }
}
'''

block_creation_with_duplicate_name_response = {
  "errors": [
    {
      "message": "Ec Block already exists",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "createBlock"
      ]
    }
  ],
  "data": {
    "createBlock": null
  }
}

create_block_with_non_existing_office = '''
mutation{
  createBlock(officeId:56 name:"Block F" ) {
    block{
      officeId
        name
      }
  }
}
'''

create_block_with_non_existing_office_response = {
    "errors": [
        {
            "message": "Office not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createBlock"
            ]
        }
    ],
    "data": {
        "createBlock": null
    }
}

update_block = '''
mutation{
  updateBlock(name: "Block A", blockId: 1){
    block{
      name
      id
    }
  }
}
'''


update_block_response = {
    "data": {
        "updateBlock": {
            "block": {
                "name": "Block A",
                "id": "1"
            }
        }
    }
}

delete_block = '''
mutation{
  DeleteBlock(blockId:1){
    block{
      name
      id
    }
  }
}
'''

delete_block_response = {
    "data": {
        "DeleteBlock": {
            "block": {
                "name": "Ec",
                "id": "1"
            }
        }
    }
}

delete_non_existent_block = '''
mutation{
  DeleteBlock(blockId:431){
    block{
      name
      id
    }
  }
}
'''

delete_non_existent_block_response = {
    "errors": [
        {
            "message": "Block not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "DeleteBlock"
            ]
        }
    ],
    "data": {
        "DeleteBlock": null
    }
}


update_non_existent_block = '''
mutation{
  updateBlock(name: "Block A", blockId: 423){
    block{
      name
      id
    }
  }
}

'''

update_non_existent_block_response = {
    "errors": [
        {
            "message": "Block not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "updateBlock"
            ]
        }
    ],
    "data": {
        "updateBlock": null
    }
}

create_block_query_with_non_nairobi_id = '''
  mutation{
  createBlock(officeId:1, name:"blask" ) {
    block{
      officeId
        name
      }
  }
}
'''
response_for_create_block_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 3
                }
                ],
            "path": [
                "createBlock"
            ]
        }
    ],
    "data": {"createBlock": null}}

response_for_delete_block_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 3
                }
                ],
            "path": [
                "DeleteBlock"
            ]
        }
    ],
    "data": {"DeleteBlock": null}}

response_for_update_block_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 3
                }
                ],
            "path": [
                "updateBlock"
            ]
        }
    ],
    "data": {"updateBlock": null}}