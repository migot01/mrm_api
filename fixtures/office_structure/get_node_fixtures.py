get_node_query = '''
query {
    getNode(nodeId: 1) {
      name
      level
      left
      right
      id
    }
}
'''

get_node_query_response = {
    "data": {
        "getNode": {
            "name": "location",
            "level": 1,
            "left": 1,
            "right": 4,
            "id": "1"
        }
    }
}

get_node_non_existant_id_query = '''
query {
    getNode(nodeId: 100) {
      name
      level
      left
      right
      id
    }
}
'''

get_node_with_non_existant_id_response = "Node not found"
