from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import MultiMatch
from .fileUtils import readDataFromindexJson, fileExists

elasticIndex = "patentimgs"


def eSearchIndexData(data):
    client = Elasticsearch()
    newPatent = {
        "patentID": data['img-patentID'],
        "pid": 'p-00'+data['img-figId'],
        "is_multiple": "0",
        "origreftext": "FIG. "+data['img-figId'],
        "figid": data['img-figId'], 
        "subfig": "", 
        "is_caption": "0", 
        "description": data['img-desc'], 
        "aspect": data['img-aspect'], 
        "object": data['img-obj']
    }
    response = client.index(
        index = elasticIndex,
        doc_type = '_doc',
        body = newPatent
    )
    print('--> ', response)
    if response['result'] == "created":
        print('--> created')
        return True
    else:
        return False

def eSearchUpdateIndex():
    return ''

def eSearchNormalRetrieve(searchTerm=""):
    client = Elasticsearch()
    q = MultiMatch(query=searchTerm, fields=['patentID', 'pid','origreftext','description','aspect', 'object'], fuzziness='AUTO')
    s = Search(using=client, index=elasticIndex).query(q)[0:20]
    response = s.execute()
    print('Total hits found : ', response.hits.total)
    search=get_results(response)
    return search

def eSearchAdvancedRetrieve(imgPatentId="", imgDescription="", imgObject="", imgAspect=""):
    client = Elasticsearch()
    q = Q("bool", 
          should=[
              Q("match", patentID=imgPatentId),
              Q("match", description=imgDescription),
              Q("match", object=imgObject),
              Q("match", aspect=imgAspect),
            ],
          minimum_should_match=1)
    s = Search(using=client, index=elasticIndex).query(q)[0:20]
    response = s.execute()
    print('Total hits found : ', response.hits.total)
    search=get_results(response)
    return search

def get_results(response):
    results=[]
    for hit in response:
        imgPathDB = fileExists('dataset/images/'+hit['patentID']+'-D0'+hit['pid'][2:]+'.png', hit['pid'])
        result_tuple = (hit.patentID, hit.pid, hit.origreftext, hit.aspect, hit.object, imgPathDB)
        results.append(result_tuple)
    return results


def bulkUploadData():
    client = Elasticsearch()
    patentData = readDataFromindexJson(BULK_JSON_DATA_FILE)
    helpers.bulk(client, patentData, index=elasticIndex)
    

if __name__ == '__main__':
    print("Opal guy details: \n",eSearch(firstName="opal"))
    print("the first 20 Female gender details: \n", eSearch(gender="f"))