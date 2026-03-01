class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        note = Counter(ransomNote)
        magazine = Counter(magazine)
        
        # print(f"{note}\n-----{magazine}")
        for k, v in note.items(): 
            if k in magazine: 
                while magazine[k] > 0 and note[k] > 0:
                    note[k] -= 1 
                    magazine[k] -= 1 
                    
        # print(f"AFter:\n{note}\n-----{magazine}")

        return True if sum(note.values()) == 0 else False