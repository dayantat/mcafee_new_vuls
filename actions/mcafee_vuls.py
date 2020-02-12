from lib.mcafee_vuls_lib import McAfee_Vuls_Lib


from st2common.runners.base_action import Action

class McAfee_New_Vuls(Action):


    def run(self, days):
        try:
            conn = McAfee_Vuls_Lib()
            items = conn.run(days)
            return True, items
        except Exception as e:
            return False, {'error':e}

