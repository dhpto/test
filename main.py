import os
import sys
import types

def main():
    print("[*] Initializing memory execution wrapper...")
    raw_script_code = os.getenv("SECURE_DECRYPT_CODE")
    
    if not raw_script_code:
        print("[-] Critical Error: SECURE_DECRYPT_CODE environment variable not found.")
        sys.exit(1)
        
    try:
        protected_module = types.ModuleType("dynamic_sports_generator")
        exec(raw_script_code, protected_module.__dict__)
        print("[+] Secure context loaded in memory. Executing payload...")
        
        # Call the main function from the hidden script
        protected_module.generate_playlist()
        
    except Exception as err:
        print(f"[-] Execution error within secure runtime layer: {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()
