from input_utils import ask_for_number


class DynamicRanges:
    lower_limit_message = 'Please type the lower limit: '
    highest_limit_message = 'Please type the highest limit: '
    invalid_highest_message = 'Please type a number greater than {}.'
    number_message = 'Please type any number: '
    goodbye_message = 'The number is between {} and {}, thanks for playing.'
    retry_message = 'The number is not between {} and {}, please try again.'

    def ask_for_lower_limit(self):
        self.lower_limit = ask_for_number(self.lower_limit_message)

    def ask_for_highest_limit(self):
        while True:
            self.highest_limit = ask_for_number(self.highest_limit_message)

            if self.highest_limit > self.lower_limit:
                break

            print(self.invalid_highest_message.format(self.lower_limit))

    def ask_for_number(self):
        self.number = ask_for_number(self.number_message)

    def play(self):
        while True:
            self.ask_for_lower_limit()
            self.ask_for_highest_limit()
            self.ask_for_number()

            if self.number >= self.lower_limit and self.number <= self.highest_limit:
                print(self.goodbye_message.format(self.lower_limit, self.highest_limit))
                break

            print(self.retry_message.format(self.lower_limit, self.highest_limit))
