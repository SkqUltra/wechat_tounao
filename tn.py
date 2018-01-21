from mitmproxy import ctx
import sys
import json
from pymongo import MongoClient

def response(flow):
	path = flow.request.path
	if path == "/question/bat/findQuiz":
		data = json.loads(flow.response.content)
		question = data["data"]["quiz"]
		options = data["data"]["options"]
		ctx.log.info("question:%s" % question)
		connection = MongoClient("mongodb://127.0.0.1:27017/")
		qus = connection["tn"]
		ans = qus.ans.find_one({"quiz":question})
		if ans != None:
			ansopt = ans["options"][ans["answer"]-1]
			ind = 1
			for opt in options:
				if opt == ansopt:
					ctx.log.info("ans:%s, index:%s" % (ansopt, ind))
					break
				else:
					ind += 1
		else:
			insData = data["data"]
			insData["answer"] = 99
			qus.ans.insert(insData)
			ctx.log.info("No question:%s" % question)
	elif path == "/question/bat/choose":
		connection = MongoClient("mongodb://127.0.0.1:27017/")
		qus=connection["tn"]		
		needAns = qus.ans.find_one({"answer":99})
		if needAns != None:
			ansData = json.loads(flow.response.content)
			needAns["answer"] = ansData["data"]["answer"]
			qus.ans.remove({"answer":99})
			qus.ans.insert(needAns)