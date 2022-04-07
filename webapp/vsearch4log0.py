def log_request(req:'flask_request', res:str) -> None:
with open('vsearch.log', 'a') as log:
print(str(dir(req)), res, file=log)
