# If your call numbers are not sequential (has multiple parts
# you can copy and paste your call numbers here (seperate with commas and quotation marks).
# Your output will appear in the output folder. 

from docx import Document
from docx.enum.text import WD_BREAK
import re
from docx.shared import Pt
from docx.oxml.ns import qn


output_path = 'template labeling/ output/'

def add_page_break(paragraph):
    paragraph.add_run().add_break(WD_BREAK.PAGE)

def save_partial_doc(doc, output_path, start_num, end_num):
    doc.save(f"{output_path}_{start_num}_to_{end_num}.docx")

def update_numbers_in_docx(file_path, output_path, values):
    numbers_per_page = 30
    max_numbers_per_file = 80

    def update_numbers(text, values, index):
        pattern = r'AWM SC \d+(\(\d+\))?'  # Adjust the pattern to match the full text
        def replacement(match):
            nonlocal index
            if index < len(values):
                updated_number = values[index]
                index += 1
                return updated_number
            else:
                return match.group(0)
        new_text = re.sub(pattern, replacement, text)
        return new_text, index

    def format_run(run):
        run.bold = True
        run.font.name = 'Arial'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
        run.font.size = Pt(11)

    def process_paragraphs(paragraphs, values, index):
        number_count = 0
        for paragraph in paragraphs:
            new_text, index = update_numbers(paragraph.text, values, index)
            if new_text != paragraph.text:
                paragraph.clear()
                run = paragraph.add_run(new_text)
                format_run(run)
            number_count += len(re.findall(r'AWM SC \d+(\(\d+\))?', paragraph.text))
            if number_count >= numbers_per_page:
                add_page_break(paragraph)
                number_count = 0
        return index

    total_values = len(values)
    current_start = 0

    while current_start < total_values:
        current_end = min(current_start + max_numbers_per_file, total_values)
        index = current_start

        doc = Document(file_path)
        index = process_paragraphs(doc.paragraphs, values, index)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    index = process_paragraphs(cell.paragraphs, values, index)

        output_file = f"{output_path}_{values[current_start]}_to_{values[current_end - 1]}.docx"
        save_partial_doc(doc, output_file, values[current_start], values[current_end - 1])

        current_start = current_end
# Example usage
input_file = 'template labeling/input.docx'
output_path = 'template labeling/ output'
values = [
    "AWM SC 12770(1)", "AWM SC 12770(2)", "AWM SC 12771", "AWM SC 12772", "AWM SC 12773", 
    "AWM SC 12774", "AWM SC 12775", "AWM SC 12776", "AWM SC 12777", "AWM SC 12778(1)", 
    "AWM SC 12778(2)", "AWM SC 12779", "AWM SC 12780", "AWM SC 12781(1)", "AWM SC 12781(2)", 
    "AWM SC 12782", "AWM SC 12783", "AWM SC 12784", "AWM SC 12785", "AWM SC 12786", 
    "AWM SC 12787", "AWM SC 12788", "AWM SC 12789", "AWM SC 12790(1)", "AWM SC 12790(2)", 
    "AWM SC 12790(3)", "AWM SC 12791", "AWM SC 12792(1)", "AWM SC 12792(2)", "AWM SC 12793", 
    "AWM SC 12794", "AWM SC 12795", "AWM SC 12796", "AWM SC 12797", "AWM SC 12798", 
    "AWM SC 12799(1)", "AWM SC 12799(2)", "AWM SC 12800", "AWM SC 12801", "AWM SC 12802", 
    "AWM SC 12803", "AWM SC 12804", "AWM SC 12805", "AWM SC 12806", "AWM SC 12807", 
    "AWM SC 12808", "AWM SC 12809(1)", "AWM SC 12809(2)", "AWM SC 12810", "AWM SC 12811(1)", 
    "AWM SC 12811(2)", "AWM SC 12812", "AWM SC 12813", "AWM SC 12814", "AWM SC 12815", 
    "AWM SC 12816", "AWM SC 12817", "AWM SC 12818", "AWM SC 12819(1)", "AWM SC 12819(2)", 
    "AWM SC 12820(1)", "AWM SC 12820(2)", "AWM SC 12821(1)", "AWM SC 12821(2)", "AWM SC 12822", 
    "AWM SC 12823", "AWM SC 12824", "AWM SC 12825", "AWM SC 12826", "AWM SC 12827(1)", 
    "AWM SC 12827(2)", "AWM SC 12828(1)", "AWM SC 12828(2)", "AWM SC 12829", "AWM SC 12830(1)", 
    "AWM SC 12830(2)", "AWM SC 12830(3)", "AWM SC 12831(1)", "AWM SC 12831(2)", "AWM SC 12831(3)", 
    "AWM SC 12832(1)", "AWM SC 12832(2)", "AWM SC 12832(3)", "AWM SC 12833", "AWM SC 12834(1)", 
    "AWM SC 12834(2)", "AWM SC 12835(1)", "AWM SC 12835(2)", "AWM SC 12835(3)", "AWM SC 12836", 
    "AWM SC 12837", "AWM SC 12838", "AWM SC 12839", "AWM SC 12840", "AWM SC 12841", "AWM SC 12842", 
    "AWM SC 12843", "AWM SC 12844", "AWM SC 12845", "AWM SC 12846", "AWM SC 12847", "AWM SC 12848", 
    "AWM SC 12849(1)", "AWM SC 12849(2)", "AWM SC 12850", "AWM SC 12851(1)", "AWM SC 12851(2)", 
    "AWM SC 12851(3)", "AWM SC 12852(1)", "AWM SC 12852(2)", "AWM SC 12853(1)", "AWM SC 12853(2)", 
    "AWM SC 12854(1)", "AWM SC 12854(2)", "AWM SC 12854(3)", "AWM SC 12855", "AWM SC 12856", 
    "AWM SC 12857(1)", "AWM SC 12857(2)", "AWM SC 12857(3)", "AWM SC 12858(1)", "AWM SC 12858(2)", 
    "AWM SC 12858(3)", "AWM SC 12859", "AWM SC 12860", "AWM SC 12861", "AWM SC 12862(1)", 
    "AWM SC 12862(2)", "AWM SC 12862(3)", "AWM SC 12863(1)", "AWM SC 12863(2)", "AWM SC 12864(1)", 
    "AWM SC 12864(2)", "AWM SC 12864(3)", "AWM SC 12865", "AWM SC 12866", "AWM SC 12867", 
    "AWM SC 12868(1)", "AWM SC 12868(2)", "AWM SC 12869(1)", "AWM SC 12869(2)", "AWM SC 12870", 
    "AWM SC 12871", "AWM SC 12872", "AWM SC 12873", "AWM SC 12874(1)", "AWM SC 12874(2)", 
    "AWM SC 12875(1)", "AWM SC 12875(2)", "AWM SC 12876(1)", "AWM SC 12876(2)", "AWM SC 12876(3)", 
    "AWM SC 12877", "AWM SC 12878", "AWM SC 12879(1)", "AWM SC 12879(2)", "AWM SC 12880(1)", 
    "AWM SC 12880(2)", "AWM SC 12881(1)", "AWM SC 12881(2)", "AWM SC 12882", "AWM SC 12883(1)", 
    "AWM SC 12883(2)", "AWM SC 12884(1)", "AWM SC 12884(2)", "AWM SC 12885", "AWM SC 12886(1)", 
    "AWM SC 12886(2)", "AWM SC 12887", "AWM SC 12888", "AWM SC 12889", "AWM SC 12890(1)", 
    "AWM SC 12890(2)", "AWM SC 12891", "AWM SC 12892", "AWM SC 12893", "AWM SC 12894", 
    "AWM SC 12895(1)", "AWM SC 12895(2)", "AWM SC 12896", "AWM SC 12897", "AWM SC 12898", 
    "AWM SC 12899", "AWM SC 12900", "AWM SC 12901", "AWM SC 12902", "AWM SC 12903", "AWM SC 12904", 
    "AWM SC 12905", "AWM SC 12906(1)", "AWM SC 12906(2)", "AWM SC 12907", "AWM SC 12908(1)", 
    "AWM SC 12908(2)", "AWM SC 12909(1)", "AWM SC 12909(2)", "AWM SC 12910(1)", "AWM SC 12910(2)", 
    "AWM SC 12911", "AWM SC 12912(1)", "AWM SC 12912(2)", "AWM SC 12913(1)", "AWM SC 12913(2)", 
    "AWM SC 12914", "AWM SC 12915", "AWM SC 12916", "AWM SC 12917", "AWM SC 12918", "AWM SC 12919(1)", 
    "AWM SC 12919(2)", "AWM SC 12920", "AWM SC 12921", "AWM SC 12922(1)", "AWM SC 12922(2)", 
    "AWM SC 12923", "AWM SC 12924(1)", "AWM SC 12924(2)", "AWM SC 12924(3)", "AWM SC 12925(1)", 
    "AWM SC 12925(2)", "AWM SC 12926", "AWM SC 12927", "AWM SC 12928", "AWM SC 12929", "AWM SC 12930", 
    "AWM SC 12931", "AWM SC 12932", "AWM SC 12933", "AWM SC 12934", "AWM SC 12935", "AWM SC 12936", 
    "AWM SC 12937", "AWM SC 12938(1)", "AWM SC 12938(2)", "AWM SC 12938(3)", "AWM SC 12939", 
    "AWM SC 12940", "AWM SC 12941", "AWM SC 12942", "AWM SC 12943(1)", "AWM SC 12943(2)", 
    "AWM SC 12944(1)", "AWM SC 12944(2)", "AWM SC 12945", "AWM SC 12946", "AWM SC 12947", "AWM SC 12948", 
    "AWM SC 12949(1)", "AWM SC 12949(2)", "AWM SC 12950(1)", "AWM SC 12950(2)", "AWM SC 12951", 
    "AWM SC 12952", "AWM SC 12953(1)", "AWM SC 12953(2)", "AWM SC 12954(1)", "AWM SC 12954(2)", 
    "AWM SC 12955", "AWM SC 12956", "AWM SC 12957(1)", "AWM SC 12957(2)", "AWM SC 12958(1)", 
    "AWM SC 12958(2)", "AWM SC 12959(1)", "AWM SC 12959(2)", "AWM SC 12960", "AWM SC 12961", 
    "AWM SC 12962(1)", "AWM SC 12962(2)", "AWM SC 12963", "AWM SC 12964(1)", "AWM SC 12964(2)", 
    "AWM SC 12965(1)", "AWM SC 12965(2)", "AWM SC 12966", "AWM SC 12967(1)", "AWM SC 12967(2)", 
    "AWM SC 12967(3)", "AWM SC 12968(1)", "AWM SC 12968(2)", "AWM SC 12969(1)", "AWM SC 12969(2)", 
    "AWM SC 12970(1)", "AWM SC 12970(2)", "AWM SC 12971", "AWM SC 12972", "AWM SC 12973", 
    "AWM SC 12974(1)", "AWM SC 12974(2)", "AWM SC 12975(1)", "AWM SC 12975(2)", "AWM SC 12976(1)", 
    "AWM SC 12976(2)", "AWM SC 12977(1)", "AWM SC 12977(2)", "AWM SC 12977(3)", "AWM SC 12978", 
    "AWM SC 12979(1)", "AWM SC 12979(2)", "AWM SC 12980(1)", "AWM SC 12980(2)", "AWM SC 12981", 
    "AWM SC 12982(1)", "AWM SC 12982(2)", "AWM SC 12982(3)", "AWM SC 12983", "AWM SC 12984", 
    "AWM SC 12985(1)", "AWM SC 12985(2)", "AWM SC 12986", "AWM SC 12987(1)", "AWM SC 12987(2)", 
    "AWM SC 12987(3)", "AWM SC 12988", "AWM SC 12989", "AWM SC 12990", "AWM SC 12991", "AWM SC 12992", 
    "AWM SC 12993(1)", "AWM SC 12993(2)", "AWM SC 12994", "AWM SC 12995(1)", "AWM SC 12995(2)", 
    "AWM SC 12996", "AWM SC 12997", "AWM SC 12998", "AWM SC 12999", "AWM SC 13000", "AWM SC 13001", 
    "AWM SC 13002", "AWM SC 13003", "AWM SC 13004(1)", "AWM SC 13004(2)", "AWM SC 13004(3)", 
    "AWM SC 13005", "AWM SC 13006", "AWM SC 13007", "AWM SC 13008", "AWM SC 13009", "AWM SC 13010", 
    "AWM SC 13011", "AWM SC 13012", "AWM SC 13013", "AWM SC 13014", "AWM SC 13015", "AWM SC 13016(1)", 
    "AWM SC 13016(2)", "AWM SC 13017", "AWM SC 13018(1)", "AWM SC 13018(2)", "AWM SC 13018(3)", 
    "AWM SC 13019(1)", "AWM SC 13019(2)", "AWM SC 13019(3)", "AWM SC 13020(1)", "AWM SC 13020(2)", 
    "AWM SC 13020(3)", "AWM SC 13021(1)", "AWM SC 13021(2)", "AWM SC 13022(1)", "AWM SC 13022(2)", 
    "AWM SC 13022(3)", "AWM SC 13023(1)", "AWM SC 13023(2)", "AWM SC 13023(3)", "AWM SC 13024(1)", 
    "AWM SC 13024(2)", "AWM SC 13025", "AWM SC 13026", "AWM SC 13027", "AWM SC 13028", "AWM SC 13029", 
    "AWM SC 13030", "AWM SC 13031", "AWM SC 13032", "AWM SC 13033", "AWM SC 13034", "AWM SC 13035", 
    "AWM SC 13036", "AWM SC 13037", "AWM SC 13038", "AWM SC 13039", "AWM SC 13040", "AWM SC 13041", 
    "AWM SC 13042", "AWM SC 13043", "AWM SC 13044", "AWM SC 13045", "AWM SC 13046", "AWM SC 13047", 
    "AWM SC 13048", "AWM SC 13049", "AWM SC 13050", "AWM SC 13051", "AWM SC 13052", "AWM SC 13053(1)", 
    "AWM SC 13053(2)", "AWM SC 13054(1)", "AWM SC 13054(2)", "AWM SC 13054(3)", "AWM SC 13055(1)", 
    "AWM SC 13055(2)", "AWM SC 13056(1)", "AWM SC 13056(2)", "AWM SC 13056(3)", "AWM SC 13057(1)", 
    "AWM SC 13057(2)", "AWM SC 13058(1)", "AWM SC 13058(2)", "AWM SC 13059(1)", "AWM SC 13059(2)", 
    "AWM SC 13060(1)", "AWM SC 13060(2)", "AWM SC 13061(1)", "AWM SC 13061(2)", "AWM SC 13062", 
    "AWM SC 13063", "AWM SC 13064", "AWM SC 13065", "AWM SC 13066", "AWM SC 13067", "AWM SC 13068(1)", 
    "AWM SC 13068(2)", "AWM SC 13069", "AWM SC 13070", "AWM SC 13071(1)", "AWM SC 13071(2)", 
    "AWM SC 13071(3)", "AWM SC 13072(1)", "AWM SC 13072(2)", "AWM SC 13073(1)", "AWM SC 13073(2)", 
    "AWM SC 13074(1)", "AWM SC 13074(2)", "AWM SC 13074(3)", "AWM SC 13075", "AWM SC 13076", 
    "AWM SC 13077(1)", "AWM SC 13077(2)", "AWM SC 13077(3)", "AWM SC 13078(1)", "AWM SC 13078(2)", 
    "AWM SC 13079", "AWM SC 13080", "AWM SC 13081(1)", "AWM SC 13081(2)", "AWM SC 13082(1)", 
    "AWM SC 13082(2)", "AWM SC 13083(1)", "AWM SC 13083(2)", "AWM SC 13084", "AWM SC 13085(1)", 
    "AWM SC 13085(2)", "AWM SC 13086", "AWM SC 13087(1)", "AWM SC 13087(2)", "AWM SC 13088(1)", 
    "AWM SC 13088(2)", "AWM SC 13089", "AWM SC 13090(1)", "AWM SC 13090(2)", "AWM SC 13091(1)", 
    "AWM SC 13091(2)", "AWM SC 13092(1)", "AWM SC 13092(2)", "AWM SC 13093", "AWM SC 13094", 
    "AWM SC 13095", "AWM SC 13096(1)", "AWM SC 13096(2)", "AWM SC 13097(1)", "AWM SC 13097(2)", 
    "AWM SC 13098(1)", "AWM SC 13098(2)", "AWM SC 13099(1)", "AWM SC 13099(2)", "AWM SC 13099(3)", 
    "AWM SC 13100(1)", "AWM SC 13100(2)", "AWM SC 13101(1)", "AWM SC 13101(2)", "AWM SC 13102(1)", 
    "AWM SC 13102(2)", "AWM SC 13103(1)", "AWM SC 13103(2)", "AWM SC 13104(1)", "AWM SC 13104(2)", 
    "AWM SC 13105(1)", "AWM SC 13105(2)", "AWM SC 13106(1)", "AWM SC 13106(2)", "AWM SC 13107(1)", 
    "AWM SC 13107(2)", "AWM SC 13108(1)", "AWM SC 13108(2)", "AWM SC 13109", "AWM SC 13110(1)", 
    "AWM SC 13110(2)", "AWM SC 13111", "AWM SC 13112", "AWM SC 13113(1)", "AWM SC 13113(2)", 
    "AWM SC 13113(3)", "AWM SC 13114(1)", "AWM SC 13114(2)", "AWM SC 13114(3)", "AWM SC 13115(1)", 
    "AWM SC 13115(2)", "AWM SC 13116", "AWM SC 13117(1)", "AWM SC 13117(2)", "AWM SC 13118", 
    "AWM SC 13119", "AWM SC 13120", "AWM SC 13121(1)", "AWM SC 13121(2)", "AWM SC 13122(1)", 
    "AWM SC 13122(2)", "AWM SC 13123", "AWM SC 13124", "AWM SC 13125", "AWM SC 13126", "AWM SC 13127(1)", 
    "AWM SC 13127(2)", "AWM SC 13128", "AWM SC 13129", "AWM SC 13130", "AWM SC 13131", "AWM SC 13132", 
    "AWM SC 13133", "AWM SC 13134", "AWM SC 13135", "AWM SC 13136(1)", "AWM SC 13136(2)", "AWM SC 13137", 
    "AWM SC 13138", "AWM SC 13139", "AWM SC 13140", "AWM SC 13141(1)", "AWM SC 13141(2)", 
    "AWM SC 13142(1)", "AWM SC 13142(2)", "AWM SC 13142(3)", "AWM SC 13142(4)", "AWM SC 13142(5)", 
    "AWM SC 13143(1)", "AWM SC 13143(2)", "AWM SC 13144(1)", "AWM SC 13144(2)", "AWM SC 13144(3)", 
    "AWM SC 13145(1)", "AWM SC 13145(2)", "AWM SC 13146(1)", "AWM SC 13146(2)", "AWM SC 13146(3)", 
    "AWM SC 13147(1)", "AWM SC 13147(2)", "AWM SC 13147(3)", "AWM SC 13148", "AWM SC 13149", 
    "AWM SC 13150", "AWM SC 13151", "AWM SC 13152(1)", "AWM SC 13152(2)", "AWM SC 13152(3)", 
    "AWM SC 13153", "AWM SC 13154", "AWM SC 13155(1)", "AWM SC 13155(2)", "AWM SC 13156(1)", 
    "AWM SC 13156(2)", "AWM SC 13157", "AWM SC 13158", "AWM SC 13159", "AWM SC 13160", "AWM SC 13161(1)", 
    "AWM SC 13161(2)", "AWM SC 13162(1)", "AWM SC 13162(2)", "AWM SC 13162(3)", "AWM SC 13163(1)", 
    "AWM SC 13163(2)", "AWM SC 13164", "AWM SC 13165", "AWM SC 13166(1)", "AWM SC 13166(2)", 
    "AWM SC 13167(1)", "AWM SC 13167(2)", "AWM SC 13167(3)", "AWM SC 13168(1)", "AWM SC 13168(2)", 
    "AWM SC 13169(1)", "AWM SC 13169(2)", "AWM SC 13170(1)", "AWM SC 13170(2)", "AWM SC 13171", 
    "AWM SC 13172", "AWM SC 13173", "AWM SC 13174", "AWM SC 13175(1)", "AWM SC 13175(2)", "AWM SC 13176", 
    "AWM SC 13177(1)", "AWM SC 13177(2)", "AWM SC 13178(1)", "AWM SC 13178(2)", "AWM SC 13179(1)", 
    "AWM SC 13179(2)", "AWM SC 13180", "AWM SC 13181", "AWM SC 13182", "AWM SC 13183", "AWM SC 13184(1)", 
    "AWM SC 13184(2)", "AWM SC 13185", "AWM SC 13186", "AWM SC 13187", "AWM SC 13188", "AWM SC 13189", 
    "AWM SC 13190", "AWM SC 13191", "AWM SC 13192(1)", "AWM SC 13192(2)", "AWM SC 13192(3)", 
    "AWM SC 13193(1)", "AWM SC 13193(2)", "AWM SC 13194", "AWM SC 13195(1)", "AWM SC 13195(2)", 
    "AWM SC 13196", "AWM SC 13197", "AWM SC 13198", "AWM SC 13199(1)", "AWM SC 13199(2)", "AWM SC 13199(3)", 
    "AWM SC 13199(4)", "AWM SC 13200", "AWM SC 13201", "AWM SC 13202", "AWM SC 13203(1)", "AWM SC 13203(2)", 
    "AWM SC 13204", "AWM SC 13205", "AWM SC 13206", "AWM SC 13207", "AWM SC 13208", "AWM SC 13209", 
    "AWM SC 13210", "AWM SC 13211", "AWM SC 13212(1)", "AWM SC 13212(2)", "AWM SC 13213(1)", 
    "AWM SC 13213(2)", "AWM SC 13213(3)", "AWM SC 13214", "AWM SC 13215", "AWM SC 13216", "AWM SC 13217", 
    "AWM SC 13218", "AWM SC 13219", "AWM SC 13220", "AWM SC 13221", "AWM SC 13222", "AWM SC 13223", 
    "AWM SC 13224(1)", "AWM SC 13224(2)", "AWM SC 13225(1)", "AWM SC 13225(2)", "AWM SC 13225(3)", 
    "AWM SC 13226(1)", "AWM SC 13226(2)", "AWM SC 13226(3)", "AWM SC 13227", "AWM SC 13228", 
    "AWM SC 13229(1)", "AWM SC 13229(2)", "AWM SC 13229(3)", "AWM SC 13230", "AWM SC 13231(1)", 
    "AWM SC 13231(2)", "AWM SC 13232(1)", "AWM SC 13232(2)", "AWM SC 13233(1)", "AWM SC 13233(2)", 
    "AWM SC 13233(3)", "AWM SC 13234(1)", "AWM SC 13234(2)", "AWM SC 13234(3)", "AWM SC 13235", 
    "AWM SC 13236", "AWM SC 13237", "AWM SC 13238", "AWM SC 13239(1)", "AWM SC 13239(2)", "AWM SC 13240", 
    "AWM SC 13241", "AWM SC 13242", "AWM SC 13243(1)", "AWM SC 13243(2)", "AWM SC 13244(1)", 
    "AWM SC 13244(2)", "AWM SC 13245(1)", "AWM SC 13245(2)", "AWM SC 13246", "AWM SC 13247", 
    "AWM SC 13248", "AWM SC 13249", "AWM SC 13250(1)", "AWM SC 13250(2)", "AWM SC 13251", "AWM SC 13252(1)", 
    "AWM SC 13252(2)", "AWM SC 13253", "AWM SC 13254", "AWM SC 13255", "AWM SC 13256", "AWM SC 13257", 
    "AWM SC 13258", "AWM SC 13259", "AWM SC 13260", "AWM SC 13261", "AWM SC 13262(1)", "AWM SC 13262(2)", 
    "AWM SC 13263", "AWM SC 13264", "AWM SC 13265(1)", "AWM SC 13265(2)", "AWM SC 13266(1)", 
    "AWM SC 13266(2)", "AWM SC 13266(3)", "AWM SC 13267(1)", "AWM SC 13267(2)", "AWM SC 13268(1)", 
    "AWM SC 13268(2)", "AWM SC 13269", "AWM SC 13270(1)", "AWM SC 13270(2)", "AWM SC 13271(1)", 
    "AWM SC 13271(2)", "AWM SC 13272(1)", "AWM SC 13272(2)", "AWM SC 13273(1)", "AWM SC 13273(2)", 
    "AWM SC 13274(1)", "AWM SC 13274(2)", "AWM SC 13275", "AWM SC 13276", "AWM SC 13277", "AWM SC 13278", 
    "AWM SC 13279", "AWM SC 13280", "AWM SC 13281", "AWM SC 13282", "AWM SC 13283", "AWM SC 13284", 
    "AWM SC 13285", "AWM SC 13286", "AWM SC 13287", "AWM SC 13288", "AWM SC 13289"
]


update_numbers_in_docx(input_file, output_path, values)

