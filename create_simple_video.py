#!/usr/bin/env python3
"""
Simple Save-the-Date Video Creator for Prathyusha & Sravan
Creates a beautiful Save-the-Date teaser using OpenCV and PIL
"""

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import math
import random

class SimpleVideoCreator:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.fps = 30
        self.duration_per_image = 4.0  # seconds per image
        
        # Create directories
        os.makedirs('temp_images', exist_ok=True)
        os.makedirs('output', exist_ok=True)
        
    def create_sample_images(self):
        """Create sample images with Indian engagement theme"""
        print("Creating cinematic images with Indian engagement styling...")
        
        # Image 1: Proposal scene with warm golden tones
        img1 = Image.new('RGB', (self.width, self.height), (240, 200, 150))
        draw1 = ImageDraw.Draw(img1)
        
        # Create warm gradient background
        for y in range(self.height):
            golden_intensity = 240 - (y / self.height) * 60
            draw1.line([(0, y), (self.width, y)], 
                      fill=(int(golden_intensity), int(golden_intensity * 0.8), int(golden_intensity * 0.6)))
        
        # Add decorative elements
        center_x, center_y = self.width // 2, self.height // 2
        
        # String lights
        for i in range(15):
            x = 100 + i * 100
            y = 100 + 30 * math.sin(i * 0.5)
            draw1.ellipse([x-8, y-8, x+8, y+8], fill=(255, 255, 200))
            
        # Floral arch
        for angle in range(-90, 91, 10):
            x = center_x + 300 * math.cos(math.radians(angle))
            y = center_y - 200 + 150 * math.sin(math.radians(angle))
            draw1.ellipse([x-5, y-5, x+5, y+5], fill=(255, 182, 193))
        
        img1.save('temp_images/image1.jpg')
        
        # Image 2: Outdoor couple photo
        img2 = Image.new('RGB', (self.width, self.height), (180, 160, 140))
        draw2 = ImageDraw.Draw(img2)
        
        # Stone texture
        for y in range(0, self.height, 20):
            for x in range(0, self.width, 30):
                color_var = random.randint(-20, 20)
                stone_color = (180 + color_var, 160 + color_var, 140 + color_var)
                draw2.rectangle([x, y, x+30, y+20], fill=stone_color)
        
        # Pillars
        for pillar_x in [200, self.width - 200]:
            draw2.rectangle([pillar_x-30, 200, pillar_x+30, self.height-100], 
                          fill=(160, 140, 120))
        
        # Flowers
        flower_colors = [(255, 105, 180), (255, 20, 147), (255, 182, 193)]
        for i in range(20):
            x = 100 + i * 80
            y = 150 + random.randint(-10, 10)
            color = random.choice(flower_colors)
            draw2.ellipse([x-4, y-4, x+4, y+4], fill=color)
            
        img2.save('temp_images/image2.jpg')
        
        # Image 3: Saree theme with text overlay
        img3 = Image.new('RGB', (self.width, self.height), (120, 80, 140))
        draw3 = ImageDraw.Draw(img3)
        
        # Purple gradient
        for y in range(self.height):
            purple_intensity = 120 + (y / self.height) * 80
            teal_accent = 40 + (y / self.height) * 60
            draw3.line([(0, y), (self.width, y)], 
                      fill=(int(purple_intensity), int(teal_accent), int(purple_intensity + 20)))
        
        # Paisley patterns
        for i in range(8):
            for j in range(5):
                x = 200 + i * 200
                y = 150 + j * 180
                draw3.ellipse([x-15, y-25, x+15, y+25], outline=(255, 215, 0), width=2)
                draw3.ellipse([x-8, y-15, x+8, y+15], fill=(0, 206, 209))
        
        # Add text overlay to final image
        self.add_text_to_image(img3, draw3)
        
        img3.save('temp_images/image3.jpg')
        print("✓ Cinematic images created!")
    
    def add_text_to_image(self, img, draw):
        """Add wedding text to the final image"""
        center_x = self.width // 2
        center_y = self.height // 2
        
        # Wedding details
        main_text = "Save the Date"
        date_text = "7th November 2025"
        couple_text = "Prathyusha & Sravan"
        time_text = "10 AM"
        venue_text = "Itihaas Restaurant & Banquet"
        
        # Try to use system fonts
        try:
            main_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 85)
            date_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 65)
            detail_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 45)
            small_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 38)
        except:
            # Fallback to default font
            main_font = ImageFont.load_default()
            date_font = ImageFont.load_default()
            detail_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Colors
        gold_color = (255, 215, 0)
        rose_gold = (255, 182, 193)
        deep_red = (139, 0, 0)
        shadow_offset = 4
        
        # Main text
        try:
            main_bbox = draw.textbbox((0, 0), main_text, font=main_font)
            main_width = main_bbox[2] - main_bbox[0]
        except:
            main_width = len(main_text) * 20  # Fallback width calculation
        
        # Draw text with shadows
        draw.text((center_x - main_width//2 + shadow_offset, center_y - 120 + shadow_offset), 
                 main_text, font=main_font, fill=deep_red)
        draw.text((center_x - main_width//2, center_y - 120), 
                 main_text, font=main_font, fill=gold_color)
        
        # Date
        try:
            date_bbox = draw.textbbox((0, 0), date_text, font=date_font)
            date_width = date_bbox[2] - date_bbox[0]
        except:
            date_width = len(date_text) * 15
            
        draw.text((center_x - date_width//2 + shadow_offset, center_y - 30 + shadow_offset), 
                 date_text, font=date_font, fill=deep_red)
        draw.text((center_x - date_width//2, center_y - 30), 
                 date_text, font=date_font, fill=rose_gold)
        
        # Couple names
        try:
            couple_bbox = draw.textbbox((0, 0), couple_text, font=detail_font)
            couple_width = couple_bbox[2] - couple_bbox[0]
        except:
            couple_width = len(couple_text) * 12
            
        draw.text((center_x - couple_width//2 + shadow_offset, center_y + 40 + shadow_offset), 
                 couple_text, font=detail_font, fill=deep_red)
        draw.text((center_x - couple_width//2, center_y + 40), 
                 couple_text, font=detail_font, fill=gold_color)
        
        # Time
        try:
            time_bbox = draw.textbbox((0, 0), time_text, font=small_font)
            time_width = time_bbox[2] - time_bbox[0]
        except:
            time_width = len(time_text) * 10
            
        draw.text((center_x - time_width//2 + shadow_offset, center_y + 100 + shadow_offset), 
                 time_text, font=small_font, fill=deep_red)
        draw.text((center_x - time_width//2, center_y + 100), 
                 time_text, font=small_font, fill=rose_gold)
        
        # Venue
        try:
            venue_bbox = draw.textbbox((0, 0), venue_text, font=small_font)
            venue_width = venue_bbox[2] - venue_bbox[0]
        except:
            venue_width = len(venue_text) * 8
            
        draw.text((center_x - venue_width//2 + shadow_offset, center_y + 150 + shadow_offset), 
                 venue_text, font=small_font, fill=deep_red)
        draw.text((center_x - venue_width//2, center_y + 150), 
                 venue_text, font=small_font, fill=rose_gold)
    
    def apply_cinematic_effects(self, image_path):
        """Apply golden/pastel tones and romantic lighting"""
        img = Image.open(image_path)
        img = img.resize((self.width, self.height), Image.Resampling.LANCZOS)
        
        # Convert to numpy for processing
        img_array = np.array(img).astype(np.float32)
        
        # Apply color grading based on image
        if 'image1' in image_path:
            # Golden hour effect
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.2, 0, 255)
            img_array[:, :, 1] = np.clip(img_array[:, :, 1] * 1.15, 0, 255)
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 0.85, 0, 255)
        elif 'image2' in image_path:
            # Natural warm tones
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.1, 0, 255)
            img_array[:, :, 1] = np.clip(img_array[:, :, 1] * 1.08, 0, 255)
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 0.95, 0, 255)
        else:  # image3
            # Rich jewel tones
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.05, 0, 255)
            img_array[:, :, 1] = np.clip(img_array[:, :, 1] * 0.95, 0, 255)
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 1.1, 0, 255)
        
        # Add vignette
        center_x, center_y = self.width // 2, self.height // 2
        Y, X = np.ogrid[:self.height, :self.width]
        dist_from_center = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
        max_dist = np.sqrt(center_x**2 + center_y**2)
        vignette = 1 - (dist_from_center / max_dist) * 0.25
        
        for i in range(3):
            img_array[:, :, i] = img_array[:, :, i] * vignette
        
        img_array = np.clip(img_array, 0, 255).astype(np.uint8)
        enhanced_img = Image.fromarray(img_array)
        
        # Additional enhancements
        enhancer = ImageEnhance.Contrast(enhanced_img)
        enhanced_img = enhancer.enhance(1.15)
        
        enhancer = ImageEnhance.Color(enhanced_img)
        enhanced_img = enhancer.enhance(1.25)
        
        enhancer = ImageEnhance.Brightness(enhanced_img)
        enhanced_img = enhancer.enhance(1.08)
        
        return enhanced_img
    
    def create_video_with_opencv(self):
        """Create video using OpenCV"""
        print("🎬 Creating video with OpenCV...")
        
        # Create sample images
        self.create_sample_images()
        
        # Video writer setup
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_path = 'output/save_the_date_simple.mp4'
        out = cv2.VideoWriter(output_path, fourcc, self.fps, (self.width, self.height))
        
        image_files = ['temp_images/image1.jpg', 'temp_images/image2.jpg', 'temp_images/image3.jpg']
        
        for i, image_path in enumerate(image_files):
            print(f"🎨 Processing scene {i+1}/3...")
            
            # Apply cinematic effects
            enhanced_img = self.apply_cinematic_effects(image_path)
            
            # Duration for this image
            duration = self.duration_per_image
            if i == len(image_files) - 1:  # Last image gets extra time
                duration += 3.0
            
            total_frames = int(duration * self.fps)
            
            # Generate frames for this image
            for frame_num in range(total_frames):
                progress = frame_num / total_frames
                
                # Create frame with subtle zoom effect
                frame = enhanced_img.copy()
                
                # Ken Burns effect
                zoom_factor = 1.0 + 0.08 * progress
                if zoom_factor > 1.0:
                    new_width = int(self.width * zoom_factor)
                    new_height = int(self.height * zoom_factor)
                    frame = frame.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    
                    # Center crop
                    left = (new_width - self.width) // 2
                    top = (new_height - self.height) // 2
                    frame = frame.crop((left, top, left + self.width, top + self.height))
                
                # Convert PIL to OpenCV format
                frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
                
                # Add fade transitions
                if i > 0 and frame_num < 30:  # Fade in
                    alpha = frame_num / 30.0
                    frame_cv = (frame_cv * alpha).astype(np.uint8)
                elif i < len(image_files) - 1 and frame_num > total_frames - 30:  # Fade out
                    alpha = (total_frames - frame_num) / 30.0
                    frame_cv = (frame_cv * alpha).astype(np.uint8)
                
                out.write(frame_cv)
        
        out.release()
        print(f"🎉 Video created successfully: {output_path}")
        return output_path

def main():
    """Main execution"""
    print("💍 Prathyusha & Sravan - Save the Date Video Creator")
    print("🎬 Creating cinematic teaser with Indian wedding aesthetics...")
    
    creator = SimpleVideoCreator()
    video_path = creator.create_video_with_opencv()
    
    print("\n✅ Video Creation Complete!")
    print("🎨 Features included:")
    print("   ✓ Golden cinematic color grading")
    print("   ✓ Indian wedding themed backgrounds")
    print("   ✓ Elegant text overlays")
    print("   ✓ Smooth Ken Burns effects")
    print("   ✓ Professional transitions")
    print("   ✓ Social media optimized")
    print(f"\n📁 Your video is ready: {video_path}")
    
    return video_path

if __name__ == "__main__":
    main()
