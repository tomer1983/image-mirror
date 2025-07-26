"""Registry operations for Image Mirror."""

import docker
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class DockerRegistry:
    def __init__(self, config: Dict):
        """Initialize DockerRegistry with configuration."""
        self.config = config
        self.client = docker.from_env()
        
    def mirror_image(self, source: str, destination: str) -> None:
        """Mirror a Docker image from source to destination."""
        try:
            # Pull the source image
            logger.info(f"Pulling source image: {source}")
            source_image = self.client.images.pull(source)
            
            # Tag the image for the destination
            logger.info(f"Tagging image for destination: {destination}")
            source_image.tag(destination)
            
            # Push to destination
            logger.info(f"Pushing image to destination: {destination}")
            self.client.images.push(destination)
            
            logger.info(f"Successfully mirrored {source} to {destination}")
            
        except docker.errors.APIError as e:
            logger.error(f"Docker API error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Failed to mirror image: {str(e)}")
            raise
