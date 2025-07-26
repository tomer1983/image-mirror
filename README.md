# Image Mirror 🔄

## Overview

**Image Mirror** is a powerful Docker image mirroring tool designed to help you efficiently mirror Docker images between different registries. It's perfect for creating backups, managing private registries, or ensuring image availability across different environments.

## Features ✨

- Mirror Docker images between different registries
- Support for various registry types (Docker Hub, Google Container Registry, Amazon ECR, etc.)
- Batch processing of multiple images
- Authentication support for private registries
- Configurable retry and timeout settings
- Detailed logging and error reporting
- Rate limiting support to prevent API throttling

## Installation 📦

### Prerequisites

- Python 3.8 or higher
- Docker CLI
- Access to source and destination registries

### Quick Start

1. Clone this repository:
```bash
git clone https://github.com/tomer1983/image-mirror.git
cd image-mirror
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🚀

### Basic Usage

Mirror a single image:
```bash
python src/image_mirror.py mirror --source docker.io/library/nginx:latest --destination private-registry.com/nginx:latest
```

Mirror multiple images from a file:
```bash
python src/image_mirror.py mirror-bulk --input images-to-import.txt --destination-registry private-registry.com
```

### Configuration

Create a `config.yaml` file to store your registry credentials and default settings:

```yaml
registries:
  source:
    url: docker.io
    username: ${DOCKER_USERNAME}
    password: ${DOCKER_PASSWORD}
  destination:
    url: private-registry.com
    username: ${DEST_USERNAME}
    password: ${DEST_PASSWORD}
```

### Setting Up Registry Credentials 🔐

There are several ways to set up your registry credentials securely:

1. **Environment Variables (Recommended for Local Development)**

   Create a `.env` file in your project root (make sure to add it to `.gitignore`):
   ```bash
   # Source registry credentials (e.g., Docker Hub)
   DOCKER_USERNAME=your_username
   DOCKER_PASSWORD=your_access_token  # Use access token instead of password when possible

   # Destination registry credentials
   DEST_USERNAME=your_destination_username
   DEST_PASSWORD=your_destination_password
   ```

2. **Docker Login (Alternative Method)**

   You can use Docker's built-in authentication:
   ```bash
   # Login to source registry (e.g., Docker Hub)
   docker login docker.io -u your_username -p your_access_token

   # Login to destination registry
   docker login private-registry.com -u your_username -p your_access_token
   ```

3. **Using Access Tokens (Recommended for Security)**

   Instead of using passwords, generate and use access tokens:
   - For Docker Hub:
     1. Go to [Docker Hub Security](https://hub.docker.com/settings/security)
     2. Click "New Access Token"
     3. Set appropriate permissions (read/write)
     4. Copy the token and use it as your password

   - For Google Container Registry (GCR):
     ```bash
     gcloud auth configure-docker
     ```

   - For Amazon ECR:
     ```bash
     aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
     ```

### Security Best Practices 🔒

1. **Never commit credentials to version control**
   ```bash
   # Add to .gitignore
   .env
   config.yaml
   ```

2. **Use least privilege access**
   - Create tokens with minimum required permissions
   - Use separate tokens for different environments

3. **Regular token rotation**
   - Rotate access tokens periodically
   - Revoke unused or compromised tokens immediately

4. **CI/CD Integration**
   When using in CI/CD pipelines:
   - Use secret management services (GitHub Secrets, GitLab CI Variables, etc.)
   - Set secrets as protected environment variables
   ```yaml
   # Example GitHub Actions secret usage
   env:
     DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
     DOCKER_PASSWORD: ${{ secrets.DOCKER_TOKEN }}
   ```

## Project Structure 📁

```
image-mirror/
├── src/                    # Source code
│   ├── __init__.py
│   ├── image_mirror.py     # Main application
│   ├── registry.py         # Registry operations
│   └── utils.py           # Utility functions
├── tests/                  # Test files
├── docs/                   # Documentation
├── images-to-import.txt    # Sample import file
├── requirements.txt        # Python dependencies
└── README.md
```

## Contributing 🤝

We love your input! We want to make contributing to Image Mirror as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

### Development Process

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the project's coding style
5. Issue that pull request!

### Running Tests

```bash
pytest tests/
```

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💬

- Create an [Issue](https://github.com/tomer1983/image-mirror/issues) for bug reports and feature requests
- For direct support, contact the maintainers

## Acknowledgments 🙏

Thanks to all contributors who have helped shape Image Mirror!


