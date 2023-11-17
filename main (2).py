def read_and_write_file(filename):
    try:
        # Read the content
        with open(filename, 'r+') as file:
            content = file.read()
            # Process the content (convert to uppercase in this case)
            processed_content = content.upper()
            # Move the file cursor to the beginning before writing
            file.seek(0)
            # Write the processed content back to the file
            file.write(processed_content)
            # Truncate the file in case the new content is shorter than the old content
            file.truncate()
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()



