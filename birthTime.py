from art import text2art # pip install art > https://pypi.org/project/art/
import datetime
import time

def main() :

    isBirth = False
    
    target_h_int = 9
    target_m_int = 29

    target_h_word = "EE"
    target_m_word = "EU"
    target_s_word = "N!"

    curr_h_int = 9
    curr_m_int = 28
    curr_s_int = 55

    while(True) : 
        curr_time = datetime.datetime.now()
        # curr_h_int = curr_time.hour
        # curr_m_int = curr_time.minute
        # curr_s_int = curr_time.second

        # if(curr_s_int == 60) :
        #     curr_h_str = target_h_int
        #     curr_m_int = target_m_int

        #     curr_s_int = 0
        
        curr_s_int += 1
        clock_str = ''
        if(curr_s_int == 60) : isBirth = True

        # if target_h_int == curr_h_int and target_m_int == curr_m_int : # 타켓 시간에 맞는 경우
        if isBirth == True : # 타켓 시간에 맞는 경우
            # 2글자씩 표기되도록 준비 (초만)
            curr_s_str = str(curr_s_int).zfill(2)

            clock_str = f'{target_h_word}:{target_m_word}:{target_s_word}'

        else : # 타겟 시간과 맞지 않는 경우
            # 2글자씩 표기되도록 준비 (시, 분, 초 전부)
            curr_h_str = str(curr_h_int).zfill(2)
            curr_m_str = str(curr_m_int).zfill(2)
            curr_s_str = str(curr_s_int).zfill(2)

            clock_str = f'{curr_h_str}:{curr_m_str}:{curr_s_str}'

        art_str = text2art(clock_str, chr_ignore=True)
        print(art_str) 
        time.sleep(1)
            
if __name__ == '__main__' :
    main()