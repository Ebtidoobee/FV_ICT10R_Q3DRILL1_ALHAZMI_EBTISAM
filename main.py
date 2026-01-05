from pyscript import document

def adding_numbers(event=None):
    if event:
        event.preventDefault()  # stop form reload

    try:
        # Get values from the input fields (default to 0 if empty)
        height1 = float(document.querySelector("#input1").value or 0)
        height2 = float(document.querySelector("#input2").value or 0)

        # Compute average
        avg = (height1 + height2) / 2

        # Output element
        output = document.querySelector("#output1")

        # Pass/Fail rule: 
        if avg >= 167.5:
            #based on the general height of a man and a woman
            output.innerHTML = f"{avg:.2f} cm -  Your type is quite common"
        else:
            output.innerHTML = f"{avg:.2f} cm -  Your type is too rare"

    except:
        document.querySelector("#output1").innerHTML = "Error!"

