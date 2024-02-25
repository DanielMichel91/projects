# Open the file "apache_logs" for reading
with open("apache_logs", "r") as file:
    # Read all lines from the file
    all_lines = file.readlines()

# Get the first line
first_line = all_lines[0]

# Split the first line into parts
parts = first_line.split()

# Print the 9th part of the first line (status code)
print(parts[8])

# Create a list to store all status codes
status_code = []

# Loop through all lines and extract status codes
for i in all_lines:
    parts = i.split()
    code = parts[8]
    status_code.append(code)

# Print the total number of status codes
print(len(status_code))

# Create a list with all status code "200"
code200 = [x for x in status_code if x == "200"]

# Print the total number of "200" status codes
print(len(code200))

# Create a list with all status code "404"
code404 = [x for x in status_code if x == "404"]

# Print the total number of "404" status codes
print(len(code404))

# Import the Counter class from the collections module
from collections import Counter

# Print a count of all unique status codes
print(Counter(status_code))

# Print the three most common status codes
print(Counter(status_code).most_common(3))

# Create a list of lines containing "404"
lines_with_404 = list(filter(lambda x: "404" in x, all_lines))

# Print the total number of lines with "404"
print(len(lines_with_404))

# Create a list of resources requested for lines with "404"
resource_list = [line.split()[6] for line in lines_with_404]

# Print the three most common resources requested for "404" status
print(Counter(resource_list).most_common(3))

# Import the PDF and seaborn libraries
from log_pdf import PDF
import seaborn as sns

# Set seaborn theme and context
sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})

# Create a histogram plot of status codes
status_code_plot = sns.histplot(status_code)
status_code_plot.set_title("Count of Status Codes")
status_code_plot.set_xlabel("Status Codes")
status_code_plot.set_ylabel("Counter")

# Save the status code plot to an image file
status_code_plot.figure.savefig('status_codes_.png', bbox_inches='tight')
status_code_plot.figure.clf()

# Create a histogram plot of resource URLs
resource_list_plot = sns.histplot(y=resource_list)
resource_list_plot.set_title("Overview")
resource_list_plot.set_xlabel("Count")
resource_list_plot.set_ylabel("URL Paths")
resource_list_plot.get_figure().set_figwidth(8)
resource_list_plot.get_figure().set_figheight(11)

# Save the resource list plot to an image file
resource_list_plot.figure.savefig('resource_list_.png', bbox_inches='tight')
resource_list_plot.figure.clf()

# Define a list of plot filenames
plots = ["status_codes_.png", "resource_list_.png"]

# Create a PDF report
log_report = PDF()

# Add each plot as a page to the report
for plot in plots:
    log_report.print_page(plot)

# Output the PDF report to "Log_Report.pdf"
log_report.output("Log_Report.pdf", "F")