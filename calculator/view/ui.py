
class UI:

  def __init__(self):
    '''
    '''

    print('New UI')

  def start(self, controller):
    '''
    We ask the user for 2 numbers.
    '''

    print('Please enter number1')
    number1 = input()

    print('Please enter number2')
    number2 = input()

    result = controller.add(int(number1), int(number2))

    print('Result:', result)

