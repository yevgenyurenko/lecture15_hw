class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, N):
        if N < 1 or N > len(self.channels):
            return "Invalid channel number"
        self.current_channel_index = N - 1
        return self.channels[self.current_channel_index]

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, query):
        if type(query) == int:
            if query >= 1 and query <= len(self.channels):
                return "Yes"
            else:
                return "No"
        elif type(query) == str:
            if query in self.channels:
                return "Yes"
            else:
                return "No"
        else:
            return "Invalid input type"

# Example usage:
channels_list = ["HBO", "CNN", "ESPN", "ABC"]
controller = TVController(channels_list)

print(controller.first_channel())          # Output: HBO
print(controller.last_channel())           # Output: ABC
print(controller.turn_channel(2))         # Output: CNN
print(controller.next_channel())          # Output: ESPN
print(controller.previous_channel())      # Output: CNN
print(controller.current_channel())       # Output: CNN
print(controller.is_exist(4))             # Output: Yes
print(controller.is_exist("BBC"))         # Output: No

    
