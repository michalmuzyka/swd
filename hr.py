import customtkinter
import json
import os
from CTkListbox import *
import openai
import asyncio
from openai import AsyncOpenAI

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Set your OpenAI API key

client = AsyncOpenAI(api_key=os.environ['CHATGPT_API_KEY'])
#client.api_key = os.environ['CHATGPT_API_KEY']
# openai.api_key = os.environ['CHATGPT_API_KEY']


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    
        self.candidates = []    
        
        # configure window
        self.title("Rekrutacja - Zespół Hr")
        self.geometry(f"{1150}x{580}")
    
        
        # team
        self.team_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.team_frame.grid(row=0, column=0, sticky="nsew")
        self.team_frame.grid_rowconfigure(5, weight=1)
        self.team_frame.grid_columnconfigure(2, weight=1)
        
        self.team_label = customtkinter.CTkLabel(self.team_frame, text="Dane o zespole", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.team_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(20, 30))
  
        self.budget_label = customtkinter.CTkLabel(self.team_frame, text="Maksymalny budżet:", font=customtkinter.CTkFont(size=14))
        self.budget_label.grid(row=1, column=0, padx=5, pady=(10, 5), sticky="nsew")
        
        self.max_budget  = customtkinter.CTkEntry(self.team_frame, placeholder_text="Maksymalny budżet")
        self.max_budget.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="nsew")
        
        self.count_label = customtkinter.CTkLabel(self.team_frame, text="Zapotrzebowanie:", font=customtkinter.CTkFont(size=14))
        self.count_label.grid(row=2, column=0, padx=5, pady=(10, 5), sticky="nsew")
        
        self.count  = customtkinter.CTkEntry(self.team_frame, placeholder_text="Liczba pracowników")
        self.count.grid(row=2, column=1, padx=(0, 10), pady=5, sticky="nsew")
        
        self.team_textbox_label = customtkinter.CTkLabel(self.team_frame, text="Kryteria zespołu:", font=customtkinter.CTkFont(size=14))
        self.team_textbox_label.grid(row=3, column=0, columnspan=2, padx=0, pady=(20, 5), sticky="nsew")
        
        self.team_textbox = customtkinter.CTkTextbox(self.team_frame, width=300)
        self.team_textbox.grid(row=4, column=0, columnspan=2, padx=(5,10), pady=5, sticky="nsew")
        
        # add candidate
                
        self.candidate_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)     
        self.candidate_frame.grid(row=0, column=1, sticky="nsew")
        self.candidate_frame.grid_rowconfigure(7, weight=1)
        self.candidate_frame.grid_columnconfigure(2, weight=1)
        
        self.add_candidate_label = customtkinter.CTkLabel(self.candidate_frame, text="Dodaj kandydata", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.add_candidate_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(20, 30))
        
        self.name_label = customtkinter.CTkLabel(self.candidate_frame, text="Imię:", font=customtkinter.CTkFont(size=14))
        self.name_label.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="nsew")
        
        self.name_entry = customtkinter.CTkEntry(self.candidate_frame, placeholder_text="Imię")
        self.name_entry.grid(row=1, column=1, padx=0, pady=5, sticky="nsew")
        
        self.surname_label = customtkinter.CTkLabel(self.candidate_frame, text="Nazwisko:", font=customtkinter.CTkFont(size=14))
        self.surname_label.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="nsew")
        
        self.surname_entry = customtkinter.CTkEntry(self.candidate_frame, placeholder_text="Nazwisko")
        self.surname_entry.grid(row=2, column=1, padx=0, pady=5, sticky="nsew")

        self.ver_label = customtkinter.CTkLabel(self.candidate_frame, text="Kod weryfikacyjny:", font=customtkinter.CTkFont(size=14))
        self.ver_label.grid(row=3, column=0, padx=10, pady=(10, 5), sticky="nsew")

        self.ver_entry = customtkinter.CTkEntry(self.candidate_frame, placeholder_text="Kod weryfikacyjny")
        self.ver_entry.grid(row=3, column=1, padx=0, pady=5, sticky="nsew")

        self.can_budget_label = customtkinter.CTkLabel(self.candidate_frame, text="Wynagrodzenie:", font=customtkinter.CTkFont(size=14))
        self.can_budget_label.grid(row=4, column=0, padx=10, pady=(10, 5), sticky="nsew")

        self.can_budget_entry = customtkinter.CTkEntry(self.candidate_frame, placeholder_text="Oczekiwane wynagrodzenie")
        self.can_budget_entry.grid(row=4, column=1, padx=0, pady=5, sticky="nsew")

        self.textbox_label = customtkinter.CTkLabel(self.candidate_frame, text="Opis kandydata:", font=customtkinter.CTkFont(size=14))
        self.textbox_label.grid(row=5, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(self.candidate_frame, width=300)
        self.textbox.grid(row=6, column=0, columnspan=2, padx=(10, 0), pady=5, sticky="nsew")

        self.add_button = customtkinter.CTkButton(master=self.candidate_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Dodaj kandydata", command=self.add_candidate)
        self.add_button.grid(row=7, column=0, columnspan=2, padx=20, pady=15, sticky="new")

        # add candidates

        self.candidates_frame = customtkinter.CTkFrame(self, width=400, corner_radius=0)
        self.candidates_frame.grid(row=0, column=2, sticky="nsew")
        self.candidates_frame.grid_rowconfigure(5, weight=1)
        
        self.candidates_frame = customtkinter.CTkLabel(self.candidates_frame, text="Kandydaci", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.candidates_frame.grid(row=0, column=0, padx=30, pady=(20, 30))
        
        self.listbox = CTkListbox(self.candidates_frame, width=400, height=200)
        self.listbox.grid(row=1, column=0, padx=20, pady=(30, 15))
        
        self.save_button = customtkinter.CTkButton(master=self.candidates_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Zapisz dane", command=self.save_data)
        self.save_button.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")

        self.save_button = customtkinter.CTkButton(master=self.candidates_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Wyznacz decyzje", command=self.calculate_decision_click)
        self.save_button.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")
        
        self.decided_label = customtkinter.CTkLabel(self.candidates_frame, text="Wybrani kandydaci:", font=customtkinter.CTkFont(size=14))
        self.decided_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(15, 5), sticky="nsew")
        
        self.decided_listbox = CTkListbox(self.candidates_frame, width=400, height=100)
        self.decided_listbox.grid(row=5, column=0, columnspan=2, padx=20, pady=(0, 5))
        
        self.load_data()

    def add_candidate(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        verification_code = self.ver_entry.get()
        budget = self.can_budget_entry.get()
        candidate_desc = self.textbox.get("1.0", 'end-1c')
        
        self.add_candidate_inner(name, surname, verification_code, budget, candidate_desc)

        self.name_entry.delete(0, customtkinter.END)
        self.surname_entry.delete(0, customtkinter.END)
        self.ver_entry.delete(0, customtkinter.END)
        self.can_budget_entry.delete(0, customtkinter.END)
        self.textbox.delete("1.0", customtkinter.END)
        
    def add_candidate_inner(self, name, surname, verification_code, budget, candidate_desc):
        self.candidates.append((name, surname, verification_code,  int(budget), candidate_desc))
        text = f"{name} - {surname} - {verification_code} - {budget} - {candidate_desc}"
        self.listbox.insert("END", text)
        
    def save_data(self):
        with open('candidates.json', 'w') as f:
            json.dump(self.candidates, f)
        with open('team.json', 'w') as f:
            json.dump([(self.max_budget.get(), self.count.get(), self.team_textbox.get("1.0", 'end-1c'))], f)
    
    def load_data(self):
        if (os.path.isfile('candidates.json')):
            with open('candidates.json') as f:
                [self.add_candidate_inner(x[0], x[1], x[2], x[3], x[4]) for x in json.load(f)]
                
        if (os.path.isfile('team.json')):
            with open('team.json') as f:
                [self.load_team_data(x[0], x[1], x[2]) for x in json.load(f)]
    
    def load_team_data(self, budget, workers_count, desc):
        self.max_budget.delete(0, customtkinter.END)
        self.max_budget.insert(0, budget)
        
        self.count.delete(0, customtkinter.END)
        self.count.insert(0, workers_count)
        
        self.team_textbox.delete("1.0", customtkinter.END)
        self.team_textbox.insert("1.0", desc)

    
    def calculate_decision_click(self):
        asyncio.run(self.calculate_decision())

    async def calculate_decision(self):
        self.save_data()
         
        candidates_json = load_from_json("candidates.json")
        decision =  await self.calculate_decision_inner(candidates_json)

        decision, candidates_json  = self.FilterCandidates(decision,candidates_json)

        self.GetBestCandidates(decision,candidates_json)

        with open('decision.json', 'w') as f:
            json.dump(decision, f)
 
        
    async def calculate_decision_inner(self,candidates_json):
        decision = [] 
        role_json = load_from_json("team.json")

        system_message = {
            "role": "system",
            "content": f"""You are an assistant that helps calculate how well candidates fit (fit score) a given role based on salary and skills. Please ensure that the score is calculated and returned as a floating-point number with exactly two decimal places. Provide a score between 0 to 1, where 1 is a candidate that has all skills. 
            Consider all candidates before giving them a score. The fourth value of candidate is his wanted salary, the smaller it is the better. Skills play the most important role when calculating the score.Return the result in JSON format where each candidate gets: [Id: , Score: ] and it is in attribute: candidates"""
        }

        calc_msg = f"""
        Calculate the score for those candidates given the role. The better the candidate, the bigger the score.

        Candidates: {candidates_json}
        Role: {role_json}
        
        Return a JSON with each candidate's fit score.
        """
        user_message = {
            "role": "user",
            "content": calc_msg
        }


        response_format_set = {
        "type": "json_schema",
        "json_schema": {
            "name": "email_score_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "Id": {
                        "description": "A unique identifier for the item (string). Read from the candidate input",
                        "type": "string"
                    },
                    "Score": {
                        "description": "A score between 0 and 1 representing the match quality",
                        "type": "number",
                        "minimum": 0,
                        "maximum": 1
                    }
                },
                "required": ["Id", "Score"],  # Ensure both properties are included
                "additionalProperties": False  # No extra properties allowed
            }
        }
        }

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages= [system_message,user_message],
            response_format= response_format_set
        )
        print(response)
        # Parse the response and return the output as JSON
        result = response.choices
        print(result)
        parsed_result = json.loads(result[0].message.content)
        decision = parsed_result["candidates"]

        print(decision)
        return decision
    
    def FilterCandidates(self, decisions,candidates):

        max_salary = float(self.max_budget.get())

        for res in decisions:
            id = res.get("Id")
            candidateInfo = next((item for item in candidates if item[2] == id),None)
            wanted_salary = candidateInfo[3]
            if(wanted_salary > max_salary):
                res["Score"] = 0
                res["Hired"] = False


        return decisions, candidates

    def GetBestCandidates(self,decisions,candidates):

        #all possible candidates
        filtered_decisions = [decision for decision in decisions if "Hired" not in decision]
        sorted_decisions = sorted(filtered_decisions, key=lambda x: x["Score"],reverse=True)

        emp_to_hire = int(self.count.get())
        top_candidates = sorted_decisions[:emp_to_hire]
        remaining_candidates = sorted_decisions[emp_to_hire:]

        #Fill
        self.decided_listbox.delete(0, "end")
        for candidate in top_candidates:
            candidate["Hired"] = True
            candidateInfo = next((item for item in candidates if item[2] == candidate["Id"]),None)
            candidate_display = f"{candidateInfo[0]} {candidateInfo[1]}"
            self.decided_listbox.insert("end",candidate_display)

        for candidate in remaining_candidates:
            candidate["Hired"] = False 

        pass




# Load candidates from candidates.json
def load_from_json(file_path):
    with open(file_path, 'r') as file:
        candidates = json.load(file)
    return candidates

if __name__ == "__main__":
    app = App()
    app.mainloop()