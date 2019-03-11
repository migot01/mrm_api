all_locations_query = '''
{
    allLocations{
        name
        abbreviation
        structure{
            name
            nestedChildren
        }
        rooms {
            name
            roomType
            capacity
            roomTags {
                name
                color
                description
            }
        }
    }
}
'''

expected_query_all_locations = {
    "data": {
        "allLocations": [
            {
                "name": "Kampala",
                "abbreviation": "KLA",
                "structure": {
                    "name": "location",
                    "nestedChildren": '{"tree_id": 1, "tag_id": null, "id": 2, "left": 2, "parent_id": 1, "level": 2, "name": "wings", "right": 3, "children": {}}'  # noqa
                },
                "rooms": [
                    {
                        "name": "Entebbe",
                        "roomType": "meeting",
                        "capacity": 6,
                        "roomTags": [
                            {
                                "name": "Block-B",
                                "color": "green",
                                "description": "The description"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Lagos",
                "abbreviation": "LOS",
                "structure": {
                    "name": "location",
                    "nestedChildren": '{"tree_id": 1, "tag_id": null, "id": 2, "left": 2, "parent_id": 1, "level": 2, "name": "wings", "right": 3, "children": {}}'  # noqa

                },
                "rooms": []
            },
            {
                "name": "Nairobi",
                "abbreviation": "NBO",
                "structure": {
                    "name": "location",
                    "nestedChildren": '{"tree_id": 1, "tag_id": null, "id": 2, "left": 2, "parent_id": 1, "level": 2, "name": "wings", "right": 3, "children": {}}'  # noqa
                },
                "rooms": []
            }
        ]
    }
}

pass_an_arg_all_locations = '''
    {
        allLocations(locationId: 1){
            name
            id
            abbreviation
        }
    }'''

expected_response_pass_an_arg = {
                                    "errors": [
                                        {
                                        "message": "Unknown argument \"locationId\" on field \"allLocations\" of type \"Query\".",  # noqa: E501
                                        "locations": [
                                            {
                                                "line": 3,
                                                "column": 22
                                                        }
                                                        ]
                                                        }
                                                        ]
                                                        }

all_location_no_hierachy = '''{
    allLocations{
        rooms {
            name
            roomType
            capacity
        }
    }
}'''

expected_all_location_no_hierachy = {
    'data': {'allLocations': [
        {'rooms': [{'name': 'Entebbe',
                    'roomType': 'meeting',
                    'capacity': 6}
                   ]},
        {'rooms': []},
        {'rooms': []}
    ]
    }
}
