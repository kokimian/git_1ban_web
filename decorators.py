def add_print_to(original):
    def wrapper():
        print("함수시작")
        original()
        print("함수 끝")
    return wrapper

@add_print_to
def print_hello():
    print("안녕하세요!")

add_print_to(print_hello())
print()
add_print_to(print_hello)()
print()
# add_print_to(print_hello())() #error



# def decorator(func):
#     def decorated(w, h):
#         if w > 0 and h > 0:
#             print("입력값 양수 확인 완료")
#             func
#             # return func(w, h) #return decorated()
#         else:
#             print("Error")
#         return decorated
#
# @decorator
# def tri_cal(w, h):
#     result = (w * h) / 2
#     return result
#
# @decorator
# def rec_cal(w, h):
#     result = w * h
#     return result
#
# tri_cal()
#
# rec_cal()
#
#
#
#
#
#
#
#
# # def decorator(func):
# #     def decorated(input_text):
# #         print('함수 시작!')
# #         func(input_text)
# #         print("함수 끝!")
# #     return decorated
# #
# # @decorator
# # def hello_world(input_text):
# #     print(input_text)
# #
# #
# # hello_world('Hello World!')