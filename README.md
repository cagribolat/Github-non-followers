# GitHub Non-Followers




## Description

This project allows you to check for GitHub users who are not following you back. It uses the GitHub API to fetch followers and following lists, then identifies users who are in your following list but not in your followers list. 

## Features

- Check non-followers on GitHub.
- Provides a web interface to input your GitHub username and personal access token.
- Allows you to create a personal access token if you don't have one.

## Technologies Used

- **Flask**: A web framework for Python used to create the web server.
- **Requests**: A Python library to make HTTP requests to the GitHub API.
- **HTML/CSS**: For creating the user interface.

## Setup

### Prerequisites

- Python 3.12 or higher
- Flask
- Requests

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/github-non-followers.git
    cd github-non-followers
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask application:**

    ```bash
    python app.py
    ```

4. **Access the web application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. Enter your GitHub username and personal access token in the provided fields.
2. Click on “Check Non-Followers” to see a list of users who are not following you back.
3. Click on “Create a Token Here if You Don’t Have One” to open the GitHub token creation page.

## Example

1. **Input Fields:**
    - **GitHub Username**: Your GitHub username.
    - **Personal Access Token**: Your GitHub personal access token.

2. **Buttons:**
    - **Check Non-Followers**: Submit the request and display the results.
    - **Create a Token Here if You Don’t Have One**: Opens GitHub’s token creation page.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, you can reach me at [cbolat2020@gmail.com](mailto:cbolat2020@gmail.com).

