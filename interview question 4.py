
def collect_failures(result, failures):
    if result["status"] != "Passed" and result["status"] != " PASSED ":
        failures.append(result["name"])
    return failures

records = [
{"name": "TC01", "status": "failed"},
{"name": "TC02", "status": "error"},
{"name": "TC01", "status": " PASSED "},
{"name": "TC03", "status": "Passed"},
{"name": "TC04", "status": "failed"},
#{"status": "failed"}
]

failures = []
for record in records:
    collect_failures(record, failures)
print(failures)


