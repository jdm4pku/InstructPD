import json
import os

def get_ner_instruct(file_path,instruct_path):
   instruct_data = []
   with open(file_path,'r',encoding='utf-8') as file:
      data = json.load(file)
   with open(instruct_path,'r',encoding='utf-8') as file:
      instruction = file.read()
   for input_item in data:
      input_text = input_item["text"]
      output_text = input_item["entity"]
      output_text = json.dumps(output_text, ensure_ascii=False)
      output_item = {
         "instruction": instruction,
         "input":input_text,
         "output":output_text
      }
      instruct_data.append(output_item)
   return instruct_data


def get_rel_instruct(file_path):
   pass

def save_file(data,path):
   json_data = json.dumps(data, ensure_ascii=False, indent=2)
   with open(path, 'w', encoding='utf-8') as output_file:
     output_file.write(json_data)

def convert_to_instruct(in_dir,output_dir,ner_instruct_path,rel_instruct_path):
    for i in range(0,10):
       train_path = os.path.join(in_dir,f"fold_{i}/train_data.json")
       test_path = os.path.join(in_dir,f"fold_{i}/test_data.json")
       train_instruct_ner = get_ner_instruct(train_path,ner_instruct_path)
       test_instruct_ner = get_ner_instruct(test_path,ner_instruct_path)
    #    train_instruct_rel = get_rel_instruct(train_path,rel_instruct_path)
    #    test_instruct_rel = get_rel_instruct(test_path,rel_instruct_path)
       train_outpath_ner = os.path.join(output_dir,f"ner/fold_{i}/train_data.json")
       test_output_ner = os.path.join(output_dir,f"ner/fold_{i}/test_data.json")
    #    train_outpath_rel = os.path.join(output_dir,f"rel/fold_{i}/train_data.json")
    #    test_output_rel = os.path.join(output_dir,f"rel/fold_{i}/test_data.json")
       save_file(train_instruct_ner,train_outpath_ner)
       save_file(test_instruct_ner,test_output_ner)
    #    save_file(train_instruct_rel,train_outpath_rel)
    #    save_file(test_instruct_rel,test_output_rel)

def main():
    in_dir = "/home/jindongming/project/modeling/InstructPD/data/origin"
    out_dir = "/home/jindongming/project/modeling/InstructPD/data/instruct"
    ner_instruct_path = "/home/jindongming/project/modeling/InstructPD/Instruct/ner_instruct.txt"
    rel_instruct_path = "/home/jindongming/project/modeling/InstructPD/Instruct/rel_instruct.txt"
    convert_to_instruct(in_dir,out_dir,ner_instruct_path,rel_instruct_path)

if __name__=="__main__":
    main()