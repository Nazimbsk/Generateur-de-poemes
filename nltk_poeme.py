import random
import nltk
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
import os

# Téléchargez et préparez les composants nécessaires de NLTK
nltk.download('punkt')


def select_random_image():
    image_files = [file for file in os.listdir('./images') if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]

    random_image = random.choice(image_files)

    return os.path.join('./images', random_image)


def add_text_to_image(poem,style, image_path):
    # Charger l'image de fond
    background_image = Image.open(image_path)

    draw = ImageDraw.Draw(background_image)

    if(style== 'sonnet') :
        font_size = 120
    else:
        font_size = 200

    font = ImageFont.truetype("arial.ttf", font_size)
    margin = 50

    poem_lines = poem.split('\n')

    total_text_height = sum(draw.textbbox((margin, 0), line, font=font)[3] - draw.textbbox((margin, 0), line, font=font)[1] for line in poem_lines)

    y_position = (background_image.size[1] - total_text_height) // 2

    for line in poem_lines:
        text_bbox = draw.textbbox((margin, y_position), line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        x_position = (background_image.size[0] - text_width) // 2

        if x_position < margin:
            x_position = margin

        draw.text((x_position, y_position), line, fill='black', font=font)

        y_position += text_height

    background_image.save('image_générée.png')










# Chargement du corpus français
with open(r'rhymes.txt', 'r', encoding='utf-8') as file:
    french_corpus = file.read()
words_list = nltk.word_tokenize(french_corpus, language='french')

# Chargement des métaphores personnalisées
with open('metaphors.txt', 'r', encoding='utf-8') as file:
    metaphors = [line.strip() for line in file]

class PoemGenerator:
 
    def __init__(self, word_list, metaphor_list):
        self.words = word_list
        self.metaphors = metaphor_list
        self.word_dict = self.build_ngram_model()

    def build_ngram_model(self):
        """Crée un modèle de trigram pour générer des textes plus cohérents."""
        word_dict = defaultdict(list)
        for word1, word2, word3 in nltk.trigrams(self.words, pad_right=True, pad_left=True):
            word_dict[(word1, word2)].append(word3)
        return word_dict

    def generate_line(self, word_count, rhyme=None):
        """Génère une ligne de poème en utilisant des trigrammes, avec la possibilité d'ajouter des rimes."""
        # Intégrer une métaphore aléatoire avec une probabilité de 30%
        if random.random() < 0.3:
            ##print( self.integrate_metaphor())

            ligne = self.integrate_metaphor()
        else :
            line = []
            seed = random.choice(list(self.word_dict.keys()))

            first_word, second_word = seed
            line.append(first_word)
            line.append(second_word)

            for _ in range(word_count - 2):
                next_word = random.choice(self.word_dict[(first_word, second_word)])
                line.append(next_word)
                first_word, second_word = second_word, next_word
            ligne = ' '.join([word for word in line if word and word.isalnum()])

        return ligne

    def integrate_metaphor(self):
        """Intègre une métaphore au hasard dans le poème."""
        return random.choice(self.metaphors)

    def generate_poem(self, style):
        """Génère un poème selon le style spécifié, intégrant une métaphore."""
        poem_lines = []
        if style == 'haiku':
            poem_lines = [self.generate_line(5), self.generate_line(7), self.generate_line(5)]

        elif style == 'free_verse':
            num_lines = random.randint(3, 7)
            poem_lines = [self.generate_line(random.randint(4, 10)) for _ in range(num_lines)]
        elif style == 'sonnet':
            poem_lines = self.generate_sonnet()

        return '\n'.join(poem_lines)

    def generate_sonnet(self):
        lines = []
        for i in range(14):
            line = self.generate_line(10) 
            lines.append(line)
        return lines








def main():
    generator = PoemGenerator(words_list, metaphors)
    while True:
            # Choix du style de poème par l'utilisateur
        style = input("Enter the style of poem (haiku, free_verse, sonnet): ").strip().lower()
        while style !=  'haiku' and style != 'free_verse' and style != 'sonnet':
            style = input("Enter the style of poem (haiku, free_verse, sonnet): ").strip().lower()
            # Génération et affichage du poème
        print("Poème généré : \n")
        poeme = generator.generate_poem(style)
        print(poeme)
        image_aleatoire = select_random_image()
        print('\n\nGénération de l\'image en cours...')
        add_text_to_image(poeme,style,image_aleatoire)

        reponse = input("\nImage générée avec succès ! Voulez-vous générer un nouveau poème ? (oui/non) : ")
        if reponse.lower() != 'oui':
            print("Merci d'avoir utilisé le générateur de poèmes. Au revoir !")
            break


main()