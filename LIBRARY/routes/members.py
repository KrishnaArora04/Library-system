from flask import Blueprint, jsonify, request
from models import members

members_blueprint = Blueprint('members', __name__)

# Add a new member
@members_blueprint.route('/', methods=['POST'])
def add_member():
    data = request.get_json()
    member_id = len(members) + 1
    data['id'] = member_id
    members.append(data)
    return jsonify(data), 201

# Get all members
@members_blueprint.route('/', methods=['GET'])
def get_members():
    return jsonify(members), 200

# Update a member
@members_blueprint.route('/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    for member in members:
        if member['id'] == member_id:
            member.update(data)
            return jsonify(member), 200
    return jsonify({'error': 'Member not found'}), 404

# Delete a member
@members_blueprint.route('/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [member for member in members if member['id'] != member_id]
    return jsonify({'message': 'Member deleted'}), 200
