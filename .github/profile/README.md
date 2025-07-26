# 🔄 Image Mirror

[![CI](https://github.com/tomer1983/image-mirror/actions/workflows/ci.yml/badge.svg)](https://github.com/tomer1983/image-mirror/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> A powerful Docker image mirroring tool for efficient container image management across registries

Image Mirror is a robust Python-based tool that simplifies the process of mirroring Docker images between different container registries. Whether you're managing private registries, creating backups, or ensuring high availability of your container images, Image Mirror makes the process seamless and efficient.

## ✨ Key Features

- 🔁 **Cross-Registry Support**: Mirror images between any combination of registries (Docker Hub, GCR, ECR, etc.)
- 📦 **Batch Processing**: Mirror multiple images at once using a simple configuration file
- 🔐 **Secure Authentication**: Built-in support for various authentication methods across different registry types
- ⚡ **Performance Optimized**: Smart retry mechanisms and concurrent transfers for efficient operations
- 📝 **Detailed Logging**: Comprehensive logging for better debugging and audit trails
- 🎯 **Rate Limiting**: Built-in rate limiting to prevent API throttling
- 🔧 **Highly Configurable**: Flexible configuration options for different use cases

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/tomer1983/image-mirror.git
cd image-mirror
pip install -r requirements.txt

# Mirror a single image
python src/image_mirror.py mirror \
  --source docker.io/library/nginx:latest \
  --destination private-registry.com/nginx:latest

# Mirror multiple images
python src/image_mirror.py mirror-bulk \
  --input images-to-import.txt \
  --destination-registry private-registry.com
```

## 📖 Documentation

Visit our [documentation](docs/) to learn more about:
- Detailed installation instructions
- Configuration options
- Advanced usage examples
- Troubleshooting guide
- API reference

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](.github/CONTRIBUTING.md) for details on how to:
- Submit bug reports
- Request features
- Submit pull requests
- Set up your development environment

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

- 📝 [Open an issue](https://github.com/tomer1983/image-mirror/issues/new/choose) for bug reports and feature requests
- 🤝 [Start a discussion](https://github.com/tomer1983/image-mirror/discussions) for questions and community support
- 🔒 [Report security vulnerabilities](.github/SECURITY.md) privately

## 🙏 Acknowledgments

Special thanks to all our contributors and the open-source community for making this project possible!
