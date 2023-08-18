import  io
from typing import Dict


def _generate_config_file_with_params (output_path: str, template_str: str, params: Dict[str, str]):
    with open(output_path, 'w', encoding='utf-8', newline='\n') as config_file:
        template_buf = io.StringIO(template_str)
        for line in template_buf:
            line = line.rstrip()
            for placeholder in params:
                if placeholder in line:
                    line = line.replace(placeholder, str(params[placeholder]))

            config_file.write(line + '\n')

def generate_config_file(output_path: str, template_str: str, collection_name: str, hdfs_path: str, *,

    solr_batch_size: int = 10000,

    num_exec: int = 10,

    exec_men: str = '10g',

    exec_core: int = 3,

    mail_recipients: str = 'sdp_core_dev, search-coe-dev'):
    _generate_config_file_with_params(output_path, template_str,{

        '<SOLR_COLLECTION>': collection_name,

        '<HDFSPATH>': hdfs_path,

        '<SOLR BATCH SIZE>': solr_batch_size,

        '<NUM EXEC>': num_exec,

        '<EXEC_NEM>': exec_men,

        '<EXEC_CORE>': exec_core,

        '<MAIL RECIPIENTS>': mail_recipients,

        })




