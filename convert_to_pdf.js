import { mdToPdf } from 'md-to-pdf';
import fs from 'fs';

const files = process.argv.slice(2).length > 0 ? process.argv.slice(2) : ['README.md', 'REGLAS_NEGOCIO.md', 'INVESTIGACION_PREVIA.md'];

(async () => {
    for (const file of files) {
        try {
            console.log(`Convirtiendo ${file}...`);
            const pdf = await mdToPdf({ path: file }, {
                launch_options: { args: ['--no-sandbox'] }
            });

            if (pdf) {
                fs.writeFileSync(file.replace('.md', '.pdf'), pdf.content);
                console.log(`✅ ${file} -> ${file.replace('.md', '.pdf')}`);
            }
        } catch (error) {
            console.error(`❌ Error al convertir ${file}:`, error);
        }
    }
})();
