# Fleet Safety Notes: setup guide

## Folder mein kya hai
- `index.html`: home page
- `dash-cam-guide.html`, `driver-risk-scores.html`: 2 original articles
- `fuel-cost-calculator.html`: free tool
- `about.html`, `contact.html`, `privacy.html`: AdSense ke liye zaroori pages
- `style.css`, `sitemap.xml`, `robots.txt`

## Step 1: Apna text check karein
- **About** aur dash cam guide ke "AI alerts" wale hisse mein aap ka apna experience likha hai. Inhein parh kar apne alfaaz mein theek kar lein.
- Agar aap company ka naam (Motive) likhna chahte hain to apna contract/NDA check kar lein. Abhi ke liye "a fleet-safety technology company" likha hai.
- Email `hello@fleetsafetynotes.co.uk` likhi hai. Ya ye email bana lein, ya apni email se replace kar dein (contact.html + privacy.html).

## Step 2: Domain lein (~£5–12/saal)
- Example: `fleetsafetynotes.co.uk`. Agar aap koi aur naam lete hain to har jagah naam aur domain badal dein (`sitemap.xml`, `robots.txt`, har page ka `canonical` link).

## Step 3: Free hosting (Cloudflare Pages)
1. github.com par nayi repo banayein aur ye saari files upload kar dein
2. dash.cloudflare.com, phir **Workers & Pages**, phir **Create**, phir **Pages**, phir apni GitHub repo connect karein
3. Build command khali chhor dein; output folder `/`
4. **Custom domains** mein apna domain add karein

## Step 4: Google Search Console
- search.google.com/search-console par site add karein aur `sitemap.xml` submit karein

## Step 5: Content barhayein, phir AdSense apply karein
- Apply karne se pehle **10–15 achhe articles** tak le jayein (ye Google ka rule nahi hai, lekin "low value content" rejection se bachne ka mehfooz tareeqa hai)
- adsense.google.com par sign up karein. Google aap ko ek `<script>` tag dega, use har page ke `<head>` mein us comment ki jagah paste kar dein: `<!-- AdSense: paste ... -->`
- Approval ke baad root mein `ads.txt` file banayein. Is ki exact line AdSense account mein milti hai.
- UK visitors ke liye **consent message** zaroori hai: AdSense ke andar **Privacy & messaging** mein free GDPR message on kar dein

## Agle articles ke ideas
1. Dual-facing vs forward-facing dash cams: kya drivers ki privacy par asar parta hai?
2. Fleet telematics kya hai? Chhoti fleet ke liye beginner guide
3. Van fleet mein harsh braking kam karne ke 7 tareeqe
4. Driver drowsiness detection kaise kaam karta hai
5. Dash cam footage insurance claim mein kaise use karein
6. Driver risk score calculator (naya tool)
