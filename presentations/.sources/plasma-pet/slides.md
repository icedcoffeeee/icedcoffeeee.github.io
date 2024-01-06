---
theme: default
transition: slide-left
layout: cover
background: mercury-vapor-lamp.jpg
class: z-10
author: Ilmi Hazim bin Saharuddin

mdc: true
presenter: true
download: false
colorSchema: 'dark'
favicon: 'https://icedcoffeeee.vercel.app/icon.png'
drawings:
    presenterOnly: true

hideInToc: true
---

<style>
h1 {
@apply
    bg-gradient-to-r
    from-teal-500
    to-green-500
    bg-clip-text
    text-transparent
    drop-shadow-lg
}
</style>

<div class="h-full w-full absolute top-0 left-0 backdrop-blur-sm -z-10"/>

<span class="z-20">SIF2019: My Plasma Pet</span>

# Mercury Vapour Lamp

Ilmi Hazim bin Saharuddin (U2000586)

---
hideInToc: true
class: text-xl
---

# Contents

<Toc/>

---
layout: image-right
image: "/mvl-intro.jpg"
---

# Introduction

A mercury vapour lamp is a

<v-clicks>

- gas discharge lamp
- used an electric arc
- vapourized mercury
- producing light!

</v-clicks>


<v-click> 

Why I chose MVLs as my Plasma Pet

</v-click> 

<v-clicks>

- Bright
- Easy to maintain
- Overall just pretty

</v-clicks>

---
layout: two-cols
clicks: 5
---

# Background Literature

<v-clicks>

- 1835: <R>Charles Wheatstone</R> observed ultravoilet lines in the mercury
  spectra from an electric discharge.
- 1860: <R>John Thomas Way</R> used arc lamps operated in a mixture of air and
  mercury vapor, creating light.
- 1896: <R>HJ Dowsing</R> and <R>HS Keating</R> became the first to patent a
  mercury vapor lamp, considered to be the first MVL.
- 1903: <R>PC Hewitt</R> improved the design by enhancing its color and
  white-balance.
- 1930: <R>General Electric</R> made the mercury vapor lamp more widespread.

</v-clicks>

::right::

<Im v-click="[1,3]" src="/mvl-dev.png" foot="Rubin, M. B. (2010). The development of the mercury lamp. Bulletin for the History of Chemistry, 35(2), 105."/>
<Im v-click="[3,5]" src="/mvl-patent.png" foot="Hewitt, P. C. (1900). Electric lamp. (U.S. Patent No. 682,690). U.S. Patent and Trademark Office. https://patents.google.com/patent/US682692"/>
<Im v-click="[5,6]" src="/mvl-general-motors.png" foot="Gendre, M. F. (2003). Two centuries of electric light source innovations. URL: http://www. einlightred. tue. nl/lightsources/history/light_history. pdf, 143."/>

---

# Fundamental Characteristics

<div class="w-full flex flex-col items-center gap-2">
    <img class="h-100 rounded-lg drop-shadow-xl" src="/mvl-practical.jpg"/>
    <span class="font-mono text-slate-400 text-center text-sm">
        Wheelan, M. (2010). The Mercury Vapor Lamp - How it works & history.
        Edison Tech Center. https://edisontechcenter.org/MercuryVaporLamps.html
    </span>
</div>

---
clicks: 4
---

# Pros and Cons

<div class="grid grid-cols-2 items-start justify-start gap-5 pt-3">
<div>
<Im adjust v-click="[1,2]" src="/mvl-spectral.jpg" foot="Davidson, M. W. (1999). ZEISS Microscopy Online Campus | Mercury Arc Lamps. https://zeiss-campus.magnet.fsu.edu/articles/lightsources/mercuryarc.html"/>
<Im left v-click="[2,3]" src="/mvl-lifetime.png" foot="Schiler, M. (1997). Simplified Design of Building Lighting, 4th Ed. USA: John Wiley and Sons. p. 27. ISBN 978-0-471-19210-7."/>
<Im adjust v-click="[3,4]" src="/mvl-paschen.png" foot="Wittenberg, H. H. (1962). Gas tube design. Electron Tube Design, 792. https://g3ynh.info/disch_tube/Wittenberg_gas_tubes.pdf"/>
<Im left v-click="[4,5]" src="/mvl-toxic.png" foot="Langford, N. J., & Ferner, R. E. (1999). Toxicity of mercury. Journal of human hypertension, 13(10), 651-656. "/>
</div>
<div>

# Pros

<v-clicks at="0">

1. High luminous efficacy (35-55 lu/W)
1. Long lifespan (~24,000 h)

</v-clicks>
<div class="h-10"/>

# Cons

<v-clicks at="2">

1. Long warm-up / cool-down time
2. Concerns of mercury content

</v-clicks>
</div>
</div>

---

# Conclusion

- MVLs have historically shown its usefulness in <R>public lighting</R> for as
  long as 100 years! (ome rural cities still rely on them)
- <R>Industrial settings</R> also favour them for their inexpensive quality.
- MVLs are also being studied as the <R>benchmark of comparison</R> when
  engineering new forms of lighting, such as LEDs.
- However, their <R>environmental effects</R> are also the main motivation
  behind the search for a better, more sustainable form of general lighting.
- The <HL>future of MVLs</HL> are more within the prospects of <R>industrial
  </R> and <R>research fields</R> rather than for general purposes.

---

# References

<div class="w-full grid grid-cols-2 gap-3 items-start">
<div>

- Rubin, M. B. (2010). The development of the mercury lamp. Bulletin for the History of Chemistry, 35(2), 105.
- Hewitt, P. C. (1900). Electric lamp. (U.S. Patent No. 682,690). U.S. Patent and Trademark Office. https://patents.google.com/patent/US682692
- Gendre, M. F. (2003). Two centuries of electric light source innovations. URL: http://www.einlightred.tue.nl/lightsources/history/light_history.pdf, 143.
- Wheelan, M. (2010). The Mercury Vapor Lamp - How it works & history. Edison Tech Center. https://edisontechcenter.org/MercuryVaporLamps.html

</div>
<div>

- Davidson, M. W. (1999). ZEISS Microscopy Online Campus | Mercury Arc Lamps. https://zeiss-campus.magnet.fsu.edu/articles/lightsources/mercuryarc.html
- Schiler, M. (1997). Simplified Design of Building Lighting, 4th Ed. USA: John Wiley and Sons. p. 27. ISBN 978-0-471-19210-7.
- Wittenberg, H. H. (1962). Gas tube design. Electron Tube Design, 792. https://g3ynh.info/disch_tube/Wittenberg_gas_tubes.pdf
- Langford, N. J., & Ferner, R. E. (1999). Toxicity of mercury. Journal of human hypertension, 13(10), 651-656. 

</div>
</div>
