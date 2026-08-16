import json
import argparse

FILEPATH  = 'data.json'

def get_json_data():
  with open(FILEPATH,"r",encoding="utf-8") as json_file:
    data = json.load(json_file)
  return data

def save_json_data(data):
  with open(FILEPATH,"w",encoding="utf-8") as outfile:
    json.dump(data, 
              outfile,
              indent=2,
              ensure_ascii=False)

def get_last_id():
    data = get_json_data()
    tasks = data.get("task",[])
    if not tasks:
      return 0
    return max(task["id"] for task in tasks)

def add_task(task_name):
  data = get_json_data()
  # pk incremental
  new_id = get_last_id() + 1
  
  data["task"].append({"id": new_id,"name":task_name})
  save_json_data(data)

if __name__ == "__main__":
  
  parser = argparse.ArgumentParser()
  parser.add_argument("command")
  parser.add_argument("task_name", nargs="?")
  args = parser.parse_args()

  if args.command == "add":
    add_task(args.task_name)

