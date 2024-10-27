from django.shortcuts import render  # Import the render function to render HTML templates
import sys  # Import the sys module to manipulate the standard input and output
import io  # Import the io module to handle input and output operations
import time  # Import the time module to measure execution time
import tracemalloc  # Import the tracemalloc module to measure memory usage

# Define the index view function
def index(request):
    # Render the 'index.html' template when the index view is accessed
    return render(request, 'index.html')

# Define the runcode view function
def runcode(request):
    # Initialize variables to store the original standard output, output, execution time, memory usage, and messages
    original_stdout = None
    output = None
    execution_time = 0
    memory_usage = 0
    memory_usage_mb = 0
    error_message = None
    success_message = None
    codeareadata = ""

    # Check if the request method is POST
    if request.method == "POST":
        # Get the code from the POST request
        codeareadata = request.POST['codearea']
        # Get the input data from the POST request, default to an empty string if not provided
        inputdata = request.POST.get('input', '')

        # Check if the code area data is empty or contains only whitespace
        if not codeareadata.strip():
            # Set an error message indicating that no code was written
            error_message = "Error: No code written."
            # Render the 'index.html' template with the provided context
            return render(request, 'index.html', {
                "code": codeareadata,
                "output": output,
                "execution_time": execution_time,
                "memory_usage": memory_usage,
                "memory_usage_mb": memory_usage_mb,
                "error_message": error_message
            })

        try:
            # Save the original standard output reference
            original_stdout = sys.stdout
            # Redirect the standard output to a file named 'file.txt'
            sys.stdout = open('file.txt', 'w')

            # Redirect the standard input to the input string
            sys.stdin = io.StringIO(inputdata)

            # Start recording the current memory usage
            tracemalloc.start()

            # Start the timer to measure execution time
            start_time = time.time()

            # Execute the code provided in the code area
            exec(codeareadata)  # Example --> print("hello world")

            # Stop the timer and calculate the execution time
            execution_time = time.time() - start_time

            # Close the redirected standard output file
            sys.stdout.close()

            # Reset the standard output to its original value
            sys.stdout = original_stdout

            # Get the current and peak memory usage
            current, peak = tracemalloc.get_traced_memory()
            # Calculate the memory usage
            memory_usage = peak - current

            # Convert the memory usage from bytes to megabytes
            memory_usage_mb = memory_usage / 10 ** 6

            # Read the output from the 'file.txt' file and save it in the output variable
            output = open('file.txt', 'r').read()

            # Set a success message indicating that the code executed correctly
            success_message = "Status: Correct Answer"
        except Exception as e:
            # In case of an exception, reset the standard output to its original value
            sys.stdout = original_stdout
            # Set the output to the exception message
            output = e
            # Clear the success message
            success_message = None

    # Render the 'index.html' template with the provided context, including code data, output, execution time, memory usage, and messages
    return render(request, 'index.html', {
        "code": codeareadata,
        "output": output,
        "execution_time": execution_time,
        "memory_usage": memory_usage,
        "memory_usage_mb": memory_usage_mb,
        "success_message": success_message,
        "error_message": error_message
    })