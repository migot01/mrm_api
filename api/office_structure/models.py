from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy_mptt.mixins import BaseNestedSets

from helpers.database import Base
from utilities.utility import Utility
from helpers.database import db_session


class OfficeStructure(Base, Utility, BaseNestedSets):
    __tablename__ = "structure"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, unique=True)
    tag_id = Column(
        Integer,
        ForeignKey('tags.id', ondelete="CASCADE"),
        nullable=True
    )

    def __repr__(self):
        return "<OfficeStructure {}>".format(self.name)

    def add_node(self, name, parent_id=None):
        """Function for adding nodes"""
        if parent_id is None:
            db_session.add(OfficeStructure(name=name))
        else:
            db_session.add(OfficeStructure(name=name, parent_id=parent_id))

        db_session.commit()

    def add_branch(self, nodes):
        """
        Function to add a single branch
        :params list of nodes
        """
        db_session.add_all(nodes)

        db_session.commit()

    @staticmethod
    def retrieve_nested_data(data):
        """
        Function to retrieve data from Office structure
        """
        nested_data = {}
        if 'children' not in data[0]:
            return nested_data
        nested_data = data[0]['children'][0]['node'].__dict__
        # Popping the _sa_instance_state because it is not needed in the
        # nested_data. This is created when the children data
        # is converted into a dictionary
        if '_sa_instance_state' in nested_data:
            nested_data.pop('_sa_instance_state')
        nested_data['children'] = OfficeStructure.retrieve_nested_data(
            data[0]['children']
        )
        return nested_data

    @property
    def nested_children(self):
        """
        Function to return a dictionary of the nested children
        """
        children = OfficeStructure.retrieve_nested_data(self.drilldown_tree())
        return children
