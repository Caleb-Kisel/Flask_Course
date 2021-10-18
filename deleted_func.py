# app.py

# @jwt.additional_claims_loader
# def add_claims_to_jwt(identity):
#     if identity == 1:
#         return {'is_admin': True}
#     return {'is_admin': False}

# claims = get_jwt()
# if not claims['is_admin']:
#     return {'message': 'Admin privileges required.'}, 401

# @jwt.expired_token_loader
# def expired_token_callback():
#     return jsonify({
#         'description': 'The token has expired.',
#         'error': 'token_expired'
#     }), 401

# @jwt.invalid_token_loader
# def invalid_token_callback():
#     return jsonify({
#         'description': 'Signature verification failed.',
#         'error': 'invalid_token'
#     }), 404

# @jwt.unauthorized_loader
# def missing_token_callback():
#     return jsonify({
#         'description': 'Request does not contain an access token.',
#         'error': 'authorization_required'
#     }), 404

# @jwt.needs_fresh_token_loader
# def token_not_fresh_callback():
#     return jsonify({
#         'description': 'The token is not fresh.',
#         'error': 'fresh_token_required'
#     }), 404

# @jwt.revoked_token_loader
# def revoked_token_callback(jwt_header, jwt_payload):
#     return jsonify({
#         'description': 'The token has been revoked',
#         'error': 'token_revoked'
#     }), 404
