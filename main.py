import json
import argparse
import shlex

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

def update(id,task_name):
  data = get_json_data()
  tasks = data.get("task",[])
  if not tasks:
    raise ValueError("there is no tasks to Update")
  for task in tasks:
    if task["id"] == id:
      tasks["name"] = task_name
      return 
  raise ValueError(f"task {id} not found")

def delete_task(id):
  return

def start_cli():
  while True:
    command_input = input("task-cli ").strip()

    parts = shlex.split(command_input)

    match parts[0]:
      case "add":
        add_task(parts[1])
      case "delete":
        delete_task(parts[1])
    
      


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("command")
  parser.add_argument("task_name", nargs="?")
  args = parser.parse_args()

  if args.command == "add":
    add_task(args.task_name)

if __name__ == "__main__":
  start_cli()
  
