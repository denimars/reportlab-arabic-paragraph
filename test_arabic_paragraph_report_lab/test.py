
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import mm
import sys
import os

# Add the parent directory of "arabic_paragraph_report_lab" to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from arabic_paragraph_report_lab.arabic_paragraph import ArabicParagraph


pdf = SimpleDocTemplate("test.pdf", pagesize=letter)

text = """بسم الله الرحمن الرحيم الحمد لله رب العالمين، والصلاة والسلام على أشرف الأنبياء والمرسلين، سيدنا محمد وعلى آله وصحبه أجمعين. أما بعد: إن اللغة العربية هي لغة الضاد، لغة القرآن الكريم، وهي من أعظم اللغات التي ميزها الله سبحانه وتعالى بجمال الأسلوب وعمق المعاني. ولقد حافظت اللغة العربية على مكانتها عبر العصور المختلفة بفضل استخدامها في العلوم والأدب والفنون. إن أهمية تعلم اللغة العربية لا تقتصر على الناطقين بها فقط، بل تمتد إلى كل من يريد فهم الإسلام وتراثه الثقافي. فهي مفتاح لفهم النصوص الدينية والشعر العربي القديم والعلوم التي أنتجتها الحضارة الإسلامية. وفي هذا السياق، يجب على المؤسسات التعليمية تعزيز مكانة اللغة العربية من خلال إدراجها في المناهج الدراسية بطرق حديثة وفعّالة. كما يجب أن نستخدم الوسائل التكنولوجية الحديثة لنشر اللغة وتعليمها للأجيال القادمة. اللهم اجعلنا من الذين يحفظون لغتهم ويعتزون بها، ويسعون لنشرها بين الناس. وبارك لنا في أوقاتنا وأعمالنا، واجعلنا من المفلحين في الدنيا والآخرة. وصلى الله وسلم وبارك على نبينا محمد وعلى آله وصحبه أجمعين. والسلام عليكم ورحمة الله وبركاته."""
x = ArabicParagraph()
table = x.ArabicParagraph(text, "amiri", "Amiri-Bold.ttf", 120*mm, 12)
pdf.build([table])
