// Website JavaScript for Save the Date
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate On Scroll)
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        offset: 100
    });

    // Hide loading screen
    setTimeout(() => {
        const loadingScreen = document.getElementById('loading-screen');
        loadingScreen.style.opacity = '0';
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500);
    }, 2000);

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    hamburger?.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger?.classList.remove('active');
            navMenu?.classList.remove('active');
        });
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Countdown timer
    updateCountdown();
    setInterval(updateCountdown, 1000);
});

// Video functions
function playVideo() {
    const video = document.getElementById('save-the-date-video');
    const overlay = document.querySelector('.video-overlay');
    
    if (video && overlay) {
        video.play();
        overlay.classList.add('hidden');
    }
}

// Countdown timer function
function updateCountdown() {
    const weddingDate = new Date('November 7, 2025 10:00:00').getTime();
    const now = new Date().getTime();
    const distance = weddingDate - now;

    if (distance > 0) {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById('days').textContent = days.toString().padStart(3, '0');
        document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
        document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
        document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
    } else {
        document.getElementById('days').textContent = '000';
        document.getElementById('hours').textContent = '00';
        document.getElementById('minutes').textContent = '00';
        document.getElementById('seconds').textContent = '00';
    }
}

// Share guide functions
function showShareGuide(platform) {
    const modal = document.getElementById('share-modal');
    const modalBody = document.getElementById('share-modal-body');
    
    const guides = {
        whatsapp: `
            <h2><i class="fab fa-whatsapp"></i> WhatsApp Sharing Guide</h2>
            <div class="guide-section">
                <h3>📱 For Status (24-hour story):</h3>
                <ol>
                    <li>Open WhatsApp on your phone</li>
                    <li>Tap <strong>"Status"</strong> at the bottom</li>
                    <li>Tap the <strong>camera icon</strong> or "My Status"</li>
                    <li>Select <strong>"Gallery"</strong> and find the video</li>
                    <li>Add text: <em>"Save the Date! 💍 Prathyusha & Sravan"</em></li>
                    <li>Tap <strong>"Send"</strong> to share with all contacts</li>
                </ol>
            </div>
            <div class="guide-section">
                <h3>💬 For Individual Chats & Groups:</h3>
                <ol>
                    <li>Open any chat or group</li>
                    <li>Tap the <strong>attachment icon</strong> (📎)</li>
                    <li>Select <strong>"Gallery"</strong> or "Photos"</li>
                    <li>Choose the Save-the-Date video</li>
                    <li>Add caption with wedding details</li>
                    <li>Send to spread the joy!</li>
                </ol>
            </div>
            <div class="guide-tip">
                <strong>💡 Pro Tip:</strong> Video is perfect size for WhatsApp (under 30 seconds)
            </div>
        `,
        instagram: `
            <h2><i class="fab fa-instagram"></i> Instagram Sharing Guide</h2>
            <div class="guide-section">
                <h3>📖 Instagram Stories:</h3>
                <ol>
                    <li>Open Instagram app</li>
                    <li><strong>Swipe right</strong> or tap your profile picture</li>
                    <li>Tap <strong>gallery icon</strong> (bottom left)</li>
                    <li>Select your Save-the-Date video</li>
                    <li>Add stickers: Date sticker, Location, Heart emojis</li>
                    <li>Tag your partner: <em>@username</em></li>
                    <li>Tap <strong>"Your Story"</strong> to share</li>
                </ol>
            </div>
            <div class="guide-section">
                <h3>📱 Instagram Feed Post:</h3>
                <ol>
                    <li>Tap the <strong>+ icon</strong> at bottom center</li>
                    <li>Select <strong>"Post"</strong></li>
                    <li>Choose video from gallery</li>
                    <li>Select cover image (thumbnail)</li>
                    <li>Add caption with hashtags:</li>
                </ol>
                <div class="hashtag-example">
                    <p><em>✨ Save the Date ✨<br><br>
                    💍 Prathyusha & Sravan<br>
                    📅 November 7th, 2025<br>
                    🕙 10 AM<br>
                    📍 Itihaas Restaurant & Banquet<br><br>
                    #SaveTheDate #IndianWedding #November2025 #PrathyushaAndSravan #WeddingAnnouncement #LoveStory</em></p>
                </div>
            </div>
            <div class="guide-section">
                <h3>🎬 Instagram Reels:</h3>
                <ol>
                    <li>Tap <strong>"Reels"</strong> at bottom</li>
                    <li>Tap camera icon then <strong>"Upload"</strong></li>
                    <li>Select your video</li>
                    <li>Add trending wedding music (optional)</li>
                    <li>Use wedding hashtags for wider reach</li>
                </ol>
            </div>
        `,
        facebook: `
            <h2><i class="fab fa-facebook-f"></i> Facebook Sharing Guide</h2>
            <div class="guide-section">
                <h3>📝 Facebook Post:</h3>
                <ol>
                    <li>Open Facebook app or website</li>
                    <li>Tap <strong>"What's on your mind?"</strong></li>
                    <li>Tap <strong>"Photo/Video"</strong></li>
                    <li>Select your Save-the-Date video</li>
                    <li>Add heartfelt caption with wedding details</li>
                    <li>Tag friends and family members</li>
                    <li>Set audience (Public, Friends, or Custom)</li>
                    <li>Click <strong>"Post"</strong> to share!</li>
                </ol>
            </div>
            <div class="guide-section">
                <h3>📖 Facebook Story:</h3>
                <ol>
                    <li>Tap <strong>"Add to Story"</strong> at top of Facebook</li>
                    <li>Select your video from gallery</li>
                    <li>Add text, stickers, or location</li>
                    <li>Share to Story (24-hour visibility)</li>
                </ol>
            </div>
            <div class="guide-section">
                <h3>🎉 Create Wedding Event:</h3>
                <ol>
                    <li>Go to <strong>"Events"</strong> in Facebook</li>
                    <li>Click <strong>"Create Event"</strong></li>
                    <li>Add details: "Wedding of Prathyusha & Sravan"</li>
                    <li>Upload your video as the event cover</li>
                    <li>Set date: November 7th, 2025</li>
                    <li>Invite all your wedding guests</li>
                </ol>
            </div>
            <div class="guide-tip">
                <strong>💡 Perfect for:</strong> Reaching extended family and friends who don't use other platforms
            </div>
        `,
        email: `
            <h2><i class="fas fa-envelope"></i> Email Sharing Guide</h2>
            <div class="guide-section">
                <h3>📧 Perfect for Older Family Members!</h3>
                <ol>
                    <li>Open your email app (Gmail, Outlook, etc.)</li>
                    <li>Click <strong>"Compose"</strong> new email</li>
                    <li>Click <strong>"Attach"</strong> and select the MP4 video file</li>
                    <li>Subject: <em>"Save the Date - Prathyusha & Sravan Wedding - November 7th, 2025"</em></li>
                    <li>Add the message below</li>
                    <li>Send to family and friends</li>
                </ol>
            </div>
            <div class="email-template">
                <h3>📝 Sample Email Message:</h3>
                <div class="email-content">
                    <p>Dear [Name],</p>
                    <p>We're thrilled to share some exciting news with you!</p>
                    <p><strong>Prathyusha and Sravan are getting married! 💍</strong></p>
                    <p><strong>📅 Date:</strong> November 7th, 2025<br>
                    <strong>🕙 Time:</strong> 10:00 AM<br>
                    <strong>📍 Venue:</strong> Itihaas Restaurant & Banquet</p>
                    <p>Please save the date and join us for this joyous celebration. We've attached a special Save-the-Date video that we created with love.</p>
                    <p>Formal wedding invitations with complete details will follow soon.</p>
                    <p>We can't wait to celebrate with you!</p>
                    <p>With love and excitement,<br>
                    [Your names]</p>
                </div>
            </div>
            <div class="guide-tip">
                <strong>💡 Great for:</strong> Family members who don't use social media, professional contacts, or detailed invitations
            </div>
        `
    };
    
    modalBody.innerHTML = guides[platform];
    modal.style.display = 'block';
}

// App guide functions
function showAppGuide(appType) {
    const modal = document.getElementById('app-modal');
    const modalBody = document.getElementById('app-modal-body');
    
    const guides = {
        gui: `
            <h2><i class="fas fa-desktop"></i> Desktop GUI Application</h2>
            <div class="guide-section">
                <h3>🖥️ User-Friendly Interface</h3>
                <p>Perfect for non-technical users who want a simple, beautiful interface.</p>
                <h4>How to Use:</h4>
                <ol>
                    <li>Download the project from GitHub</li>
                    <li>Extract the ZIP file</li>
                    <li>Double-click the right file for your system:</li>
                    <ul>
                        <li><strong>Windows:</strong> run_app.bat</li>
                        <li><strong>Mac:</strong> run_app.command</li>
                        <li><strong>Linux:</strong> run_app.sh</li>
                    </ul>
                </ol>
                <h4>Features:</h4>
                <ul>
                    <li>✅ Beautiful, easy-to-use interface</li>
                    <li>✅ One-click download to Downloads folder</li>
                    <li>✅ Choose custom download location</li>
                    <li>✅ Video preview player</li>
                    <li>✅ Step-by-step social media guides</li>
                    <li>✅ Quick actions and shortcuts</li>
                </ul>
            </div>
        `,
        web: `
            <h2><i class="fas fa-globe"></i> Web Browser Application</h2>
            <div class="guide-section">
                <h3>🌐 Works on Any Device</h3>
                <p>Great for sharing with family members - works on phones, tablets, and computers.</p>
                <h4>How to Use:</h4>
                <ol>
                    <li>Download the project</li>
                    <li>Open terminal/command prompt</li>
                    <li>Run: <code>python3 web_app.py</code></li>
                    <li>Browser opens automatically to <code>http://localhost:8080</code></li>
                    <li>Share this URL with family on the same network!</li>
                </ol>
                <h4>Features:</h4>
                <ul>
                    <li>✅ Mobile-friendly responsive design</li>
                    <li>✅ Works on any device with a browser</li>
                    <li>✅ Direct video download</li>
                    <li>✅ Video preview player</li>
                    <li>✅ Detailed sharing guides</li>
                    <li>✅ No installation needed for family</li>
                </ul>
            </div>
        `,
        cli: `
            <h2><i class="fas fa-terminal"></i> Command Line Interface</h2>
            <div class="guide-section">
                <h3>⚡ For Developers & Tech Users</h3>
                <p>Traditional command-line approach with full control.</p>
                <h4>How to Use:</h4>
                <div class="code-block">
                    <code>
                    git clone https://github.com/srijaharshikad/wedding.git<br>
                    cd wedding<br>
                    pip install -r requirements.txt<br>
                    python3 create_simple_video.py<br>
                    python3 download_video.py
                    </code>
                </div>
                <h4>Features:</h4>
                <ul>
                    <li>✅ Full control over video generation</li>
                    <li>✅ Access to all source code</li>
                    <li>✅ Customizable parameters</li>
                    <li>✅ Batch processing capabilities</li>
                    <li>✅ Perfect for automation</li>
                    <li>✅ Advanced troubleshooting</li>
                </ul>
            </div>
        `
    };
    
    modalBody.innerHTML = guides[appType];
    modal.style.display = 'block';
}

// Social sharing functions
function shareOnWhatsApp() {
    const text = encodeURIComponent("Save the Date! 💍 Prathyusha & Sravan are getting married on November 7th, 2025 at Itihaas Restaurant & Banquet. Watch our beautiful announcement: " + window.location.href);
    window.open(`https://wa.me/?text=${text}`, '_blank');
}

function shareOnFacebook() {
    const url = encodeURIComponent(window.location.href);
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank');
}

function shareOnTwitter() {
    const text = encodeURIComponent("Save the Date! 💍 Prathyusha & Sravan - November 7th, 2025");
    const url = encodeURIComponent(window.location.href);
    window.open(`https://twitter.com/intent/tweet?text=${text}&url=${url}`, '_blank');
}

function copyLink() {
    navigator.clipboard.writeText(window.location.href).then(() => {
        showToast('Link copied to clipboard!');
    }).catch(() => {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = window.location.href;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showToast('Link copied to clipboard!');
    });
}

// Download function
function downloadVideo() {
    // Try to download from the relative path first
    const videoUrl = '../output/save_the_date_simple.mp4';
    
    // Create a temporary link element
    const link = document.createElement('a');
    link.href = videoUrl;
    link.download = 'Prathyusha_Sravan_Save_The_Date.mp4';
    
    // Check if the file exists by trying to fetch it
    fetch(videoUrl, { method: 'HEAD' })
        .then(response => {
            if (response.ok) {
                // File exists, proceed with download
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                showToast('Download started! Check your Downloads folder.');
            } else {
                // File doesn't exist, show message
                showToast('Video not found! Please generate the video first using the desktop app.', 'error');
            }
        })
        .catch(() => {
            // Fallback: try to download anyway
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            showToast('Download attempted. If it fails, please use the desktop app to generate the video first.');
        });
}

// Modal functions
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const shareModal = document.getElementById('share-modal');
    const appModal = document.getElementById('app-modal');
    
    if (event.target === shareModal) {
        shareModal.style.display = 'none';
    }
    if (event.target === appModal) {
        appModal.style.display = 'none';
    }
}

// Toast notification
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');
    
    toastMessage.textContent = message;
    
    if (type === 'error') {
        toast.style.background = '#dc3545';
    } else {
        toast.style.background = '#28a745';
    }
    
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal('share-modal');
        closeModal('app-modal');
    }
});

// Add some interactive animations
function addInteractiveAnimations() {
    // Parallax effect for hero background
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('.hero-background');
        if (parallax) {
            const speed = scrolled * 0.5;
            parallax.style.transform = `translateY(${speed}px)`;
        }
    });

    // Add hover effects to cards
    const cards = document.querySelectorAll('.detail-card, .share-card, .download-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Initialize interactive animations when page loads
document.addEventListener('DOMContentLoaded', addInteractiveAnimations);
