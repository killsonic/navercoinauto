import pyautogui
import time
import sys
import keyboard # keyboard 라이브러리 추가
import os # os 모듈 추가
import sys # sys 모듈 추가 (resource_path 함수에서 사용)
import random

# --- PyAutoGUI 기본 설정 ---
pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.1 # 예시: 각 동작 후 0.1초 대기

# --- 스크립트 정지 플래그 ---
stop_script = False


# --- PyInstaller 리소스 경로 설정 함수 ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS # PyInstaller로 패키징되었을 때 임시 경로
    except Exception:
        base_path = os.path.abspath(".") # 개발 환경에서 현재 경로
    return os.path.join(base_path, relative_path)

# 이미지 파일 경로를 이 함수를 통해 가져오도록 변경
image1_path = resource_path('1.png')
image2_path = resource_path('2.png')
image3_path = resource_path('3.png') # 3.png 이미지 경로 추가
image4_path = resource_path('4.png') # 4.png 이미지 경로 추가
image5_path = resource_path('5.png') # 5.png 이미지 경로 추가


# 키보드 이벤트 핸들러 함수 정의
def on_key_event(event):
    global stop_script
    # 'esc' 키가 눌렸을 때 stop_script 플래그를 True로 설정
    if event.name == 'esc' and event.event_type == keyboard.KEY_DOWN:
        print("\n[알림] 'Esc' 키가 감지되었습니다. 잠시 후 스크립트를 종료합니다.")
        stop_script = True
        
# 'esc' 키 눌림을 감지하는 리스너 등록
keyboard.on_press(on_key_event)

# 스크립트가 시작되기 전, 마우스의 최초(전체 스크립트 기준) 위치를 한 번만 기록합니다.
# 이 위치는 스크립트가 완전히 종료될 때 마우스가 최종적으로 돌아올 위치입니다.
original_script_start_mouse_x, original_script_start_mouse_y = pyautogui.position()
print(f"스크립트 시작 전 마우스의 최초 위치: ({original_script_start_mouse_x}, {original_script_start_mouse_y})")

print("스크립트를 시작합니다.")
print("▶ 마우스를 화면 좌측 상단 모서리로 이동하거나 'Esc' 키를 누르면 언제든지 중지됩니다.")
print("작업 시작! 1.png 이미지를 찾습니다...")

try: # 전체 스크립트를 try 블록으로 감싸서 종료 시점에 마우스 복귀를 확실히 합니다.
    # 무한 반복
    while True:
        # 매 반복마다 스크립트 정지 플래그를 확인합니다.
        if stop_script:
            break # 플래그가 True이면 루프를 빠져나와 스크립트를 종료합니다.
        
        # 각 이미지 찾기 루프 시작 시점의 마우스 위치를 기록합니다.
        # 이 위치는 해당 루프의 모든 작업이 끝난 후 마우스가 돌아올 '대기' 위치가 됩니다.
        loop_start_mouse_x, loop_start_mouse_y = pyautogui.position()
        print(f"\n[새로운 루프 시작] 현재 마우스 위치: ({loop_start_mouse_x}, {loop_start_mouse_y})")

        try:
            # 1. '1.png' 이미지 찾기 시도
            location1 = pyautogui.locateOnScreen(image1_path, confidence=0.7)

            if location1: # 1.png를 찾았을 경우
                print(f"✅ '1.png' 이미지 발견! 위치: {location1}")
                
                center_x1, center_y1 = pyautogui.center(location1)
                
                pyautogui.moveTo(center_x1, center_y1, duration=0.5)
                print(f"   마우스를 ({center_x1}, {center_y1})로 이동했습니다.")
                
                pyautogui.dragRel(0, -1000, duration=1.0)
                print("   현재 위치에서 1000픽셀 위로 드래그를 완료했습니다.")
                
               
                # 드래그 완료 후 0.5초 대기
                print("▶ 드래그 완료 후 0.5초 대기합니다...")
                time.sleep(0.5) 
                
                # 마우스를 다음 이미지 찾기 대기 위치(루프 시작 위치)로 복귀
                pyautogui.moveTo(loop_start_mouse_x, loop_start_mouse_y, duration=0)
                print(f"   [정보] 마우스를 다음 대기 위치 ({loop_start_mouse_x}, {loop_start_mouse_y})로 되돌렸습니다.")

                # --- [3.png, 4.png, 그리고 5.png 로직 시작] ---
                print("\n--- '3.png', '4.png', 이미지 검색 시작 ---")
                try:                    
                    
                    #3.png 확인
                    location3 = pyautogui.locateOnScreen(image3_path, confidence=0.95)
                    if location3:
                        print(f"✅ '3.png' 이미지 발견! 위치: {location3}")
                        center_x3, center_y3 = pyautogui.center(location3)
                        pyautogui.click(center_x3, center_y3)
                        print("▶ '3.png' 발견 클릭 후 1초 대기합니다...")
                        time.sleep(1) # 1초 대기
                        
                        # 4.png 찾기 및 클릭
                        print("▶ '4.png' 이미지를 찾습니다...")
                        location4 = pyautogui.locateOnScreen(image4_path, confidence=0.7)
                        if location4:
                            print(f"✅ '4.png' 이미지 발견! 위치: {location4}")
                            center_x4, center_y4 = pyautogui.center(location4)
                            pyautogui.click(center_x4, center_y4)
                            print(f"   '4.png' 이미지를 ({center_x4}, {center_y4})에서 클릭했습니다.")
                            print("--- '3.png' 및 '4.png' 작업 완료 ---")
                        else:
                            print("❌ '4.png' 이미지를 찾지 못했습니다.")
                    else:
                        print("❌ '3.png' 이미지를 찾지 못했습니다.")

                except pyautogui.ImageNotFoundException:
                    print("   '3.png', '4.png', 검색 중 ImageNotFoundException 발생.")
                    # ImageNotFoundException이 발생하더라도 1.png 재확인 로직으로 넘어가기 위해 예외를 다시 발생시키지 않습니다.
                # --- [3.png, 4.png, 그] ---
                
                # 1.png 재확인 시도 (기존 로직)
                print("▶ 1초 대기 후 '1.png' 이미지를 다시 확인합니다...")
                try:
                    location1_recheck = pyautogui.locateOnScreen(image1_path, confidence=0.7)
                    if location1_recheck: # 1.png가 1초 대기 후에도 여전히 있다면
                        print(f"✅ '1.png' 이미지가 1초 대기 후에도 다시 발견되었습니다. 위치: {location1_recheck}")
                        print("▶ 다음 작업까지 10~15초 대기합니다...")
                        for _ in range(random.randint(10, 15)): # 대기 시간 중에도 'stop_script' 플래그를 계속 확인
                            if stop_script:
                                break
                            time.sleep(1)
                        if stop_script: # 대기 중에도 정지 요청이 들어왔다면 즉시 루프 탈출
                            break
                        print("--- '1.png' 작업을 완료하고 다음 반복으로 넘어갑니다 ---")
                        continue # 이 지점에서 다음 'while True' 루프로 넘어감

                    else: # 1.png가 1초 대기 후 사라졌다면 (locateOnScreen이 None 반환)
                        print("❌ '1.png' 이미지가 1초 대기 후 사라졌습니다. 2.png를 찾습니다.")
                        raise pyautogui.ImageNotFoundException # 2.png 로직으로 이동하기 위해 예외 발생

                except pyautogui.ImageNotFoundException:
                    # 1초 대기 후 1.png를 다시 찾지 못했을 경우, 이 예외가 발생하며 외부 except 블록으로 넘어갑니다.
                    print("❌ '1.png' 재확인 중 이미지를 찾지 못했습니다. 2.png 검색으로 전환합니다.")
                    raise # 외부 except 블록으로 예외 전달

            else: # 1.png를 처음 찾지 못했을 경우
                print("❌ '1.png' 이미지를 찾지 못했습니다. 2.png를 찾습니다...")
                raise pyautogui.ImageNotFoundException # 2.png 로직으로 이동하기 위해 예외 발생

        except (pyautogui.ImageNotFoundException, FileNotFoundError): # 1.png를 못 찾았거나, 1.png 재확인 실패 시
            # 스크립트 정지 플래그 재확인 (5.png가 이전에 발견되었을 수도 있음)
            try:
                    # 5.png를 가장 먼저 확인하여 발견 시 즉시 종료합니다.
                    location5 = pyautogui.locateOnScreen(image5_path, confidence=0.7)
                    if location5:
                        print(f"🚨 '5.png' 이미지 발견! 위치: {location5}")
                        print("[알림] '5.png' 발견으로 인해 스크립트를 즉시 종료합니다.")
                        stop_script = True # 스크립트 정지 플래그 설정
                        break # while True 루프를 빠져나와 finally 블록으로 이동
                    else:
                            print("❌ '5.png' 이미지를 찾지 못했습니다.")
            except pyautogui.ImageNotFoundException:
                    # 1초 대기 후 1.png를 다시 찾지 못했을 경우, 이 예외가 발생하며 외부 except 블록으로 넘어갑니다.
                    print("❌ '5.png' 재확인 중 이미지를 찾지 못했습니다. 2.png 검색으로 전환합니다.")

            if stop_script:
                break # 플래그가 True이면 루프를 빠져나와 스크립트를 종료합니다.

            print("--- '2.png' 이미지 검색 시작 ---")
            try:
                location2 = pyautogui.locateOnScreen(image2_path, confidence=0.7)
                if location2:
                    print(f"✅ '2.png' 이미지 발견! 위치: {location2}")
                    center_x2, center_y2 = pyautogui.center(location2)

                    # --- '2.png'에 대한 사용자님 요청 동작: 500픽셀 위로 이동 후 1000픽셀 드래그 ---
                    target_y_for_drag_start = center_y2 - 500
                    pyautogui.moveTo(center_x2, target_y_for_drag_start, duration=0.5)
                    print(f"   마우스를 '2.png' 중심에서 500픽셀 위인 ({center_x2}, {target_y_for_drag_start})로 이동했습니다.")

                    pyautogui.dragRel(0, -1000, duration=1.0) # 현재 위치에서 1000픽셀 위로 드래그 업
                    print("   현재 위치에서 1000픽셀 위로 드래그를 완료했습니다.")
                    
                    # 드래그 완료 후 0.5초 대기 (1.png와 일관성을 위해)
                    print("▶ 드래그 완료 후 0.5초 대기합니다...")
                    time.sleep(0.5)
                    
                    # 마우스를 루프 시작 위치로 복귀
                    pyautogui.moveTo(loop_start_mouse_x, loop_start_mouse_y, duration=0)
                    print(f"   [정보] 마우스를 다음 대기 위치 ({loop_start_mouse_x}, {loop_start_mouse_y})로 되돌렸습니다.")
                    
                    print("--- '2.png' 작업을 완료하고 다음 반복으로 넘어갑니다 ---")
                    time.sleep(random.uniform(1, 3)) # 다음 루프 전 1~3초 랜덤 대기
                else:
                    print("❌ '2.png' 이미지를 찾지 못했습니다. 5초 후 다시 시도합니다.")
                    time.sleep(5) # 2.png를 찾지 못했으면 5초 대기
            
            except Exception as e:
                print(f"[오류 발생] '2.png' 처리 중 예상치 못한 오류가 발생했습니다: {e}")
                print("5초 후 다시 시도합니다...")
                time.sleep(5)

except Exception as e:
    # try...except...finally 구조에서 발생한 치명적인 예외를 처리
    print(f"\n[치명적인 오류 발생] 스크립트 실행 중 오류가 발생하여 강제로 종료됩니다: {e}")
finally:
    # 스크립트가 어떤 이유로든 (정상 종료, Esc 키, 5.png 발견, 오류 발생 등)
    # 종료될 때 마우스 위치를 처음 시작했던 위치로 되돌립니다.
    print(f"\n[종료 알림] 스크립트가 종료됩니다. 마우스를 최초 시작 위치 ({original_script_start_mouse_x}, {original_script_start_mouse_y})로 되돌립니다.")
    pyautogui.moveTo(original_script_start_mouse_x, original_script_start_mouse_y, duration=0.5)
    # 키보드 리스너 해제 (스크립트 종료 시 필수)
    keyboard.unhook_all()