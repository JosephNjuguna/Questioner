@question_api.route('/questions/<string:id>/upvote',methods=["PATCH"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"please upvote a question"}),204)
  
@question_api.route('/questions',methods=["POST"])
def question_post():
    return make_response(jsonify({"message":"post questions "}),201)

@question_api.route('/questions/<string:id>/downvote',methods=["PATCH"])
def downvoteQuestion(id):
    return make_response(jsonify({"message":" downvote a question"}),204)
