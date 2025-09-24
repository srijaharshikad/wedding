#!/usr/bin/env python3
"""
Cinematic Save-the-Date Video Creator for Prathyusha & Sravan
Creates a beautiful Save-the-Date teaser with cinematic effects, Indian engagement styling,
animated floral motifs, and elegant text overlays.
"""

import numpy as np
import cv2
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
import math
import random

class SaveTheDateCreator:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.fps = 30
        self.duration_per_image = 4.0  # seconds per image
        self.transition_duration = 1.0  # seconds for transitions
        
        # Create directories
        os.makedirs('temp_images', exist_ok=True)
        os.makedirs('output', exist_ok=True)
        os.makedirs('assets', exist_ok=True)
        
    def create_sample_images(self):
        """Create sample images representing the couple's photos with Indian engagement theme"""
        print("Creating cinematic images with Indian engagement styling...")
        
        # Image 1: Proposal scene with warm golden tones
        img1 = Image.new('RGB', (self.width, self.height), (240, 200, 150))
        draw1 = ImageDraw.Draw(img1)
        
        # Create warm gradient background
        for y in range(self.height):
            golden_intensity = 240 - (y / self.height) * 60
            draw1.line([(0, y), (self.width, y)], 
                      fill=(int(golden_intensity), int(golden_intensity * 0.8), int(golden_intensity * 0.6)))
        
        # Add decorative elements suggesting engagement setting
        center_x, center_y = self.width // 2, self.height // 2
        
        # Draw string lights effect
        for i in range(15):
            x = 100 + i * 100
            y = 100 + 30 * math.sin(i * 0.5)
            draw1.ellipse([x-8, y-8, x+8, y+8], fill=(255, 255, 200))
            
        # Add floral arch suggestion
        arch_points = []
        for angle in range(-90, 91, 10):
            x = center_x + 300 * math.cos(math.radians(angle))
            y = center_y - 200 + 150 * math.sin(math.radians(angle))
            arch_points.append((x, y))
            draw1.ellipse([x-5, y-5, x+5, y+5], fill=(255, 182, 193))
        
        img1.save('temp_images/image1.jpg')
        
        # Image 2: Outdoor couple photo with stone architecture
        img2 = Image.new('RGB', (self.width, self.height), (180, 160, 140))
        draw2 = ImageDraw.Draw(img2)
        
        # Stone texture background with warm tones
        for y in range(0, self.height, 20):
            for x in range(0, self.width, 30):
                color_var = random.randint(-20, 20)
                stone_color = (180 + color_var, 160 + color_var, 140 + color_var)
                draw2.rectangle([x, y, x+30, y+20], fill=stone_color)
        
        # Add architectural elements
        # Pillars
        for pillar_x in [200, self.width - 200]:
            draw2.rectangle([pillar_x-30, 200, pillar_x+30, self.height-100], 
                          fill=(160, 140, 120))
        
        # Decorative flowers on balcony
        flower_colors = [(255, 105, 180), (255, 20, 147), (255, 182, 193)]
        for i in range(20):
            x = 100 + i * 80
            y = 150 + random.randint(-10, 10)
            color = random.choice(flower_colors)
            draw2.ellipse([x-4, y-4, x+4, y+4], fill=color)
            
        img2.save('temp_images/image2.jpg')
        
        # Image 3: Formal photo with saree theme and rich colors
        img3 = Image.new('RGB', (self.width, self.height), (120, 80, 140))
        draw3 = ImageDraw.Draw(img3)
        
        # Rich purple gradient background (inspired by saree colors)
        for y in range(self.height):
            purple_intensity = 120 + (y / self.height) * 80
            teal_accent = 40 + (y / self.height) * 60
            draw3.line([(0, y), (self.width, y)], 
                      fill=(int(purple_intensity), int(teal_accent), int(purple_intensity + 20)))
        
        # Add elegant patterns suggesting Indian textiles
        for i in range(8):
            for j in range(5):
                x = 200 + i * 200
                y = 150 + j * 180
                # Paisley-inspired patterns
                draw3.ellipse([x-15, y-25, x+15, y+25], outline=(255, 215, 0), width=2)
                draw3.ellipse([x-8, y-15, x+8, y+15], fill=(0, 206, 209, 100))
        
        img3.save('temp_images/image3.jpg')
        print("✓ Cinematic images created with Indian engagement styling!")
    
    def apply_cinematic_effects(self, image_path):
        """Apply golden/pastel tones and romantic lighting with Indian wedding aesthetics"""
        img = Image.open(image_path)
        img = img.resize((self.width, self.height), Image.Resampling.LANCZOS)
        
        # Convert to numpy array for processing
        img_array = np.array(img)
        img_array = img_array.astype(np.float32)
        
        # Apply Indian wedding color palette - warm golds and rich tones
        if 'image1' in image_path:
            # Golden hour effect for proposal scene
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.2, 0, 255)  # Enhanced reds
            img_array[:, :, 1] = np.clip(img_array[:, :, 1] * 1.15, 0, 255)  # Golden greens
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 0.85, 0, 255)   # Reduced blues
        elif 'image2' in image_path:
            # Natural warm tones for outdoor photo
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.1, 0, 255)
            img_array[:, :, 1] = np.clip(img_array[:, :, 1] * 1.08, 0, 255)
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 0.95, 0, 255)
        else:  # image3 - saree photo
            # Rich jewel tones
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.05, 0, 255)
            img_array[:, :, 1] = np.clip(img_array[:, :, 1] * 0.95, 0, 255)
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 1.1, 0, 255)
        
        # Add cinematic vignette
        center_x, center_y = self.width // 2, self.height // 2
        Y, X = np.ogrid[:self.height, :self.width]
        dist_from_center = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
        max_dist = np.sqrt(center_x**2 + center_y**2)
        vignette = 1 - (dist_from_center / max_dist) * 0.25
        
        for i in range(3):
            img_array[:, :, i] = img_array[:, :, i] * vignette
        
        img_array = np.clip(img_array, 0, 255).astype(np.uint8)
        enhanced_img = Image.fromarray(img_array)
        
        # Apply additional cinematic enhancements
        enhancer = ImageEnhance.Contrast(enhanced_img)
        enhanced_img = enhancer.enhance(1.15)
        
        enhancer = ImageEnhance.Color(enhanced_img)
        enhanced_img = enhancer.enhance(1.25)
        
        enhancer = ImageEnhance.Brightness(enhanced_img)
        enhanced_img = enhancer.enhance(1.08)
        
        return enhanced_img
    
    def create_floral_overlay(self, frame_number, total_frames):
        """Create animated Indian-inspired floral motifs"""
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        progress = frame_number / total_frames
        
        # Create floating marigold-inspired petals
        num_flowers = 16
        for i in range(num_flowers):
            # Gentle floating animation
            base_angle = (i / num_flowers) * 2 * math.pi
            radius = 350 + 80 * math.sin(progress * 1.5 * math.pi + i)
            
            x = self.width // 2 + radius * math.cos(base_angle + progress * 0.3)
            y = self.height // 2 + radius * math.sin(base_angle + progress * 0.3)
            
            # Flower size varies gently
            size = 18 + 8 * math.sin(progress * 3 * math.pi + i * 0.5)
            
            # Indian wedding flower colors
            colors = [
                (255, 165, 0, 100),    # Marigold orange
                (255, 140, 0, 100),    # Dark orange
                (255, 182, 193, 100),  # Light pink
                (255, 105, 180, 100),  # Hot pink
                (255, 215, 0, 100),    # Gold
                (220, 20, 60, 100),    # Crimson
            ]
            color = colors[i % len(colors)]
            
            # Draw lotus-inspired flower shape
            for petal in range(8):
                petal_angle = (petal / 8) * 2 * math.pi
                px1 = x + size * 0.6 * math.cos(petal_angle)
                py1 = y + size * 0.6 * math.sin(petal_angle)
                px2 = x + size * math.cos(petal_angle + 0.2)
                py2 = y + size * math.sin(petal_angle + 0.2)
                px3 = x + size * math.cos(petal_angle - 0.2)
                py3 = y + size * math.sin(petal_angle - 0.2)
                
                draw.polygon([(x, y), (px1, py1), (px2, py2)], fill=color)
                draw.polygon([(x, y), (px1, py1), (px3, py3)], fill=color)
        
        # Add corner rangoli-inspired decorations
        self.draw_rangoli_corners(draw, progress)
        
        # Add subtle sparkle effects
        self.add_sparkles(draw, progress)
        
        return overlay
    
    def draw_rangoli_corners(self, draw, progress):
        """Draw rangoli-inspired decorative elements in corners"""
        corners = [
            (100, 100),  # Top left
            (self.width - 100, 100),  # Top right
            (100, self.height - 100),  # Bottom left
            (self.width - 100, self.height - 100)  # Bottom right
        ]
        
        for corner_x, corner_y in corners:
            # Animated rangoli pattern
            for ring in range(3):
                radius = 30 + ring * 15
                alpha = int(120 * (1 - progress * 0.2))
                
                # Draw circular pattern
                for i in range(8):
                    angle = (i / 8) * 2 * math.pi + progress * math.pi
                    x = corner_x + radius * math.cos(angle)
                    y = corner_y + radius * math.sin(angle)
                    
                    color = (255, 215, 0, alpha) if ring % 2 == 0 else (255, 105, 180, alpha)
                    draw.ellipse([x-4, y-4, x+4, y+4], fill=color)
    
    def add_sparkles(self, draw, progress):
        """Add subtle sparkle effects throughout the frame"""
        num_sparkles = 20
        for i in range(num_sparkles):
            # Random but consistent positions
            random.seed(i)
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            
            # Twinkling animation
            twinkle = math.sin(progress * 4 * math.pi + i) * 0.5 + 0.5
            alpha = int(80 * twinkle)
            
            if alpha > 20:
                size = 2 + int(3 * twinkle)
                draw.ellipse([x-size, y-size, x+size, y+size], 
                           fill=(255, 255, 255, alpha))
    
    def create_text_overlay(self, progress):
        """Create elegant animated text overlay for Save the Date"""
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        # Text appears in stages for dramatic effect
        if progress > 0.6:  # Text starts appearing at 60%
            text_progress = (progress - 0.6) / 0.4
            
            # Different elements appear at different times
            main_alpha = int(255 * min((text_progress - 0.0) * 3, 1)) if text_progress > 0.0 else 0
            date_alpha = int(255 * min((text_progress - 0.2) * 3, 1)) if text_progress > 0.2 else 0
            couple_alpha = int(255 * min((text_progress - 0.4) * 3, 1)) if text_progress > 0.4 else 0
            details_alpha = int(255 * min((text_progress - 0.6) * 3, 1)) if text_progress > 0.6 else 0
            
            # Wedding details
            main_text = "Save the Date"
            date_text = "7th November 2025"
            couple_text = "Prathyusha & Sravan"
            time_text = "10 AM"
            venue_text = "Itihaas Restaurant & Banquet"
            
            # Try to use elegant fonts
            try:
                main_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 85)
                date_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 65)
                detail_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 45)
                small_font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttc", 38)
            except:
                try:
                    main_font = ImageFont.truetype("/System/Library/Fonts/Times.ttc", 85)
                    date_font = ImageFont.truetype("/System/Library/Fonts/Times.ttc", 65)
                    detail_font = ImageFont.truetype("/System/Library/Fonts/Times.ttc", 45)
                    small_font = ImageFont.truetype("/System/Library/Fonts/Times.ttc", 38)
                except:
                    main_font = ImageFont.load_default()
                    date_font = ImageFont.load_default()
                    detail_font = ImageFont.load_default()
                    small_font = ImageFont.load_default()
            
            center_x = self.width // 2
            center_y = self.height // 2
            
            # Colors for Indian wedding theme
            gold_color = (255, 215, 0)
            rose_gold = (255, 182, 193)
            deep_red = (139, 0, 0)
            
            shadow_offset = 4
            
            # Main "Save the Date" text
            if main_alpha > 0:
                main_bbox = draw.textbbox((0, 0), main_text, font=main_font)
                main_width = main_bbox[2] - main_bbox[0]
                
                # Elegant shadow
                draw.text((center_x - main_width//2 + shadow_offset, center_y - 120 + shadow_offset), 
                         main_text, font=main_font, fill=(*deep_red, main_alpha//2))
                # Main text
                draw.text((center_x - main_width//2, center_y - 120), 
                         main_text, font=main_font, fill=(*gold_color, main_alpha))
            
            # Date
            if date_alpha > 0:
                date_bbox = draw.textbbox((0, 0), date_text, font=date_font)
                date_width = date_bbox[2] - date_bbox[0]
                
                draw.text((center_x - date_width//2 + shadow_offset, center_y - 30 + shadow_offset), 
                         date_text, font=date_font, fill=(*deep_red, date_alpha//2))
                draw.text((center_x - date_width//2, center_y - 30), 
                         date_text, font=date_font, fill=(*rose_gold, date_alpha))
            
            # Couple names
            if couple_alpha > 0:
                couple_bbox = draw.textbbox((0, 0), couple_text, font=detail_font)
                couple_width = couple_bbox[2] - couple_bbox[0]
                
                draw.text((center_x - couple_width//2 + shadow_offset, center_y + 40 + shadow_offset), 
                         couple_text, font=detail_font, fill=(*deep_red, couple_alpha//2))
                draw.text((center_x - couple_width//2, center_y + 40), 
                         couple_text, font=detail_font, fill=(*gold_color, couple_alpha))
            
            # Time and venue
            if details_alpha > 0:
                time_bbox = draw.textbbox((0, 0), time_text, font=small_font)
                time_width = time_bbox[2] - time_bbox[0]
                
                draw.text((center_x - time_width//2 + shadow_offset, center_y + 100 + shadow_offset), 
                         time_text, font=small_font, fill=(*deep_red, details_alpha//2))
                draw.text((center_x - time_width//2, center_y + 100), 
                         time_text, font=small_font, fill=(*rose_gold, details_alpha))
                
                venue_bbox = draw.textbbox((0, 0), venue_text, font=small_font)
                venue_width = venue_bbox[2] - venue_bbox[0]
                
                draw.text((center_x - venue_width//2 + shadow_offset, center_y + 150 + shadow_offset), 
                         venue_text, font=small_font, fill=(*deep_red, details_alpha//2))
                draw.text((center_x - venue_width//2, center_y + 150), 
                         venue_text, font=small_font, fill=(*rose_gold, details_alpha))
        
        return overlay
    
    def create_video_clip(self, image_path, duration):
        """Create a cinematic video clip from an image with all effects"""
        enhanced_img = self.apply_cinematic_effects(image_path)
        
        def make_frame(t):
            progress = t / duration
            frame_number = int(t * self.fps)
            total_frames = int(duration * self.fps)
            
            # Start with enhanced image
            frame = enhanced_img.copy()
            
            # Subtle Ken Burns effect (zoom and pan)
            zoom_factor = 1.0 + 0.08 * progress
            new_width = int(self.width * zoom_factor)
            new_height = int(self.height * zoom_factor)
            
            if zoom_factor > 1.0:
                frame = frame.resize((new_width, new_height), Image.Resampling.LANCZOS)
                # Center crop with slight pan
                pan_x = int(10 * math.sin(progress * math.pi))
                pan_y = int(5 * math.cos(progress * math.pi))
                left = (new_width - self.width) // 2 + pan_x
                top = (new_height - self.height) // 2 + pan_y
                frame = frame.crop((left, top, left + self.width, top + self.height))
            
            # Add floral overlay
            floral_overlay = self.create_floral_overlay(frame_number, total_frames)
            frame = Image.alpha_composite(frame.convert('RGBA'), floral_overlay)
            
            # Add text overlay for the final image
            if 'image3' in image_path:
                text_overlay = self.create_text_overlay(progress)
                frame = Image.alpha_composite(frame, text_overlay)
            
            return np.array(frame.convert('RGB'))
        
        return VideoClip(make_frame, duration=duration)
    
    def create_save_the_date_video(self):
        """Create the complete cinematic Save-the-Date video"""
        print("🎬 Creating your cinematic Save-the-Date video...")
        print("✨ Features: Golden tones, floral animations, elegant transitions")
        
        # Create sample images
        self.create_sample_images()
        
        # Create clips
        clips = []
        image_files = ['temp_images/image1.jpg', 'temp_images/image2.jpg', 'temp_images/image3.jpg']
        
        for i, image_path in enumerate(image_files):
            print(f"🎨 Processing scene {i+1}/3...")
            
            clip_duration = self.duration_per_image
            if i == len(image_files) - 1:  # Last image gets extra time for text
                clip_duration += 3.0
                
            clip = self.create_video_clip(image_path, clip_duration)
            clips.append(clip)
            
            # Add crossfade transition
            if i < len(image_files) - 1:
                clips.append(clip.crossfadeout(self.transition_duration))
        
        print("🎵 Combining scenes with cinematic transitions...")
        
        # Concatenate with crossfades
        final_video = concatenate_videoclips(clips, method="compose")
        
        # Add opening and closing fades
        final_video = final_video.fadein(1.5).fadeout(2.5)
        
        print("🎶 Adding romantic background music...")
        
        # Create harmonic background music
        def make_audio(t):
            # Indian classical inspired harmonies
            fundamental = 220  # A3
            fifth = 330        # E4  
            octave = 440       # A4
            third = 277        # C#4
            
            # Create gentle chord progression
            chord1 = (0.2 * np.sin(2 * np.pi * fundamental * t) + 
                     0.15 * np.sin(2 * np.pi * fifth * t) +
                     0.1 * np.sin(2 * np.pi * octave * t))
            
            # Add subtle tabla-like rhythm
            rhythm = 0.05 * np.sin(2 * np.pi * 2 * t) * np.exp(-2 * (t % 2))
            
            # Gentle modulation for warmth
            modulation = 0.1 * np.sin(2 * np.pi * 0.3 * t)
            
            return (chord1 + rhythm) * (0.6 + modulation)
        
        audio = AudioClip(make_audio, duration=final_video.duration)
        final_video = final_video.set_audio(audio)
        
        print("📹 Exporting your cinematic Save-the-Date...")
        
        # Export final video
        output_path = "output/save_the_date_cinematic.mp4"
        final_video.write_videofile(
            output_path,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            bitrate='8000k',  # High quality for social media
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        print(f"🎉 Your cinematic Save-the-Date is ready!")
        print(f"📁 Location: {output_path}")
        print(f"⏱️  Duration: {final_video.duration:.1f} seconds")
        print(f"📱 Optimized for social media sharing!")
        
        return output_path

def main():
    """Main execution"""
    print("💍 Prathyusha & Sravan - Save the Date Video Creator")
    print("🎬 Creating cinematic teaser with Indian wedding aesthetics...")
    
    creator = SaveTheDateCreator()
    video_path = creator.create_save_the_date_video()
    
    print("\n✅ Video Creation Complete!")
    print("🎨 Features included:")
    print("   ✓ Golden cinematic color grading")
    print("   ✓ Indian wedding floral animations") 
    print("   ✓ Elegant text overlays")
    print("   ✓ Smooth Ken Burns effects")
    print("   ✓ Romantic background music")
    print("   ✓ Professional transitions")
    print("   ✓ Social media optimized")
    
    return video_path

if __name__ == "__main__":
    main()
