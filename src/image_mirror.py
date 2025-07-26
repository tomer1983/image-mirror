"""Main module for Image Mirror."""

import click
import logging
from typing import Optional
from .registry import DockerRegistry
from .utils import load_config, setup_logging

logger = logging.getLogger(__name__)

@click.group()
def cli():
    """Image Mirror CLI tool for managing Docker image mirroring."""
    pass

@cli.command()
@click.option('--source', required=True, help='Source image with tag')
@click.option('--destination', required=True, help='Destination image with tag')
@click.option('--config', default='config.yaml', help='Path to config file')
def mirror(source: str, destination: str, config: str):
    """Mirror a single Docker image from source to destination."""
    setup_logging()
    cfg = load_config(config)
    
    try:
        registry = DockerRegistry(cfg)
        registry.mirror_image(source, destination)
        click.echo(f"Successfully mirrored {source} to {destination}")
    except Exception as e:
        logger.error(f"Failed to mirror image: {str(e)}")
        raise click.ClickException(str(e))

@cli.command()
@click.option('--input', required=True, help='Input file with list of images')
@click.option('--destination-registry', required=True, help='Destination registry URL')
@click.option('--config', default='config.yaml', help='Path to config file')
def mirror_bulk(input: str, destination_registry: str, config: str):
    """Mirror multiple Docker images from a file."""
    setup_logging()
    cfg = load_config(config)
    
    try:
        registry = DockerRegistry(cfg)
        with open(input, 'r') as f:
            images = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        for image in images:
            dest_image = f"{destination_registry}/{image.split('/')[-1]}"
            try:
                registry.mirror_image(image, dest_image)
                click.echo(f"Successfully mirrored {image} to {dest_image}")
            except Exception as e:
                logger.error(f"Failed to mirror {image}: {str(e)}")
                continue
                
    except Exception as e:
        logger.error(f"Failed to process bulk mirror: {str(e)}")
        raise click.ClickException(str(e))

if __name__ == '__main__':
    cli()
