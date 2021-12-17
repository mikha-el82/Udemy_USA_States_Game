import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # adds image as a new possible turtle shape
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states_data = pandas.read_csv("50_states.csv")
# print(states_data.state)

score = 0
correct_states = []

while score < 50:
    if score == 0:
        prompt_title = "Guess the State"
        prompt_text = "Type the state's name:"
    else:
        prompt_title = f"{score}/50 States Correct"
        prompt_text = "Type another state's name:"
    answer_state = screen.textinput(title=prompt_title, prompt=prompt_text)
    # print(f"--{answer_state}--")
    if answer_state is None:
        # print("Nope...")
        break
    if answer_state == "":
        continue
    elif states_data.state.str.fullmatch(answer_state, case=False).any() \
            and answer_state.lower() not in (state.lower() for state in correct_states):
        state_row = states_data[states_data.state.str.contains(answer_state, case=False, regex=False)]
        state = state_row.iloc[0, 0]
        x_coord = state_row.iloc[0, 1]
        y_coord = state_row.iloc[0, 2]
        writer.goto(x_coord, y_coord)
        writer.write(state)
        score += 1
        correct_states.append(state)

if score == 50:
    print("Congratulations! You guessed all 50 states!")
else:
    print(f"You guessed correctly {score} of 50 states:")
    for i in range(len(correct_states)):
        print(f"{i+1} {correct_states[i]}")

turtle.bye()
