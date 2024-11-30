import os
import sys
import json
import pytest
import logging
import httpx
from typing import List, Dict, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuration
BASE_URL = "http://localhost:8000"
TEST_QUERIES = [
    {
        "category": "Контакты",
        "queries": [
            "Найти контакты ЖКХ",
            "Управляющая компания Петроградского района",
            "Телефон диспетчерской службы"
        ]
    },
    {
        "category": "Городские услуги",
        "queries": [
            "Как сообщить о проблеме с благоустройством",
            "Ремонт дорог в Санкт-Петербурге",
            "Куда жаловаться на коммунальные услуги"
        ]
    },
    {
        "category": "Образование",
        "queries": [
            "Как записать ребенка в детский сад",
            "Информация о школах Санкт-Петербурга",
            "Дополнительное образование для детей"
        ]
    },
    {
        "category": "Развлечения",
        "queries": [
            "Афиша Санкт-Петербурга",
            "Музеи и театры",
            "Культурные события этой недели"
        ]
    }
]

class EvaluationMetrics:
    @staticmethod
    def calculate_response_quality(response: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate response quality metrics
        """
        metrics = {
            "response_length": len(response.get("response", "")),
            "source_count": len(response.get("sources", [])),
            "confidence": response.get("confidence", 0.0)
        }
        
        # Additional quality scoring
        quality_score = (
            (metrics["response_length"] > 50) * 0.3 +  # Meaningful response
            (metrics["source_count"] > 0) * 0.3 +     # Has sources
            (metrics["confidence"] > 0.5) * 0.4       # High confidence
        )
        
        metrics["quality_score"] = quality_score
        return metrics

class APIEvaluator:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=base_url)
        self.results = {}
    
    def evaluate_queries(self, test_queries: List[Dict]) -> Dict:
        """
        Evaluate queries across different categories
        """
        for category_data in test_queries:
            category = category_data["category"]
            self.results[category] = {
                "queries": [],
                "avg_quality_score": 0.0,
                "total_queries": len(category_data["queries"])
            }
            
            for query in category_data["queries"]:
                query_result = self._evaluate_single_query(query)
                self.results[category]["queries"].append(query_result)
            
            # Calculate average quality score for category
            quality_scores = [
                result["metrics"]["quality_score"] 
                for result in self.results[category]["queries"]
            ]
            self.results[category]["avg_quality_score"] = (
                sum(quality_scores) / len(quality_scores) 
                if quality_scores else 0.0
            )
        
        return self.results
    
    def _evaluate_single_query(self, query: str) -> Dict:
        """
        Evaluate a single query
        """
        try:
            response = self.client.post(
                "/query", 
                json={"query": query}
            )
            response.raise_for_status()
            
            response_data = response.json()
            metrics = EvaluationMetrics.calculate_response_quality(response_data)
            
            return {
                "query": query,
                "response": response_data.get("response", ""),
                "metrics": metrics
            }
        except Exception as e:
            logging.error(f"Query evaluation error for '{query}': {e}")
            return {
                "query": query,
                "response": "",
                "metrics": {
                    "response_length": 0,
                    "source_count": 0,
                    "confidence": 0.0,
                    "quality_score": 0.0
                }
            }

@pytest.fixture(scope="module")
def api_evaluator():
    return APIEvaluator(BASE_URL)

def test_system_evaluation(api_evaluator):
    """
    Comprehensive system evaluation
    """
    results = api_evaluator.evaluate_queries(TEST_QUERIES)
    
    # Generate report
    report_path = os.path.join(
        os.path.dirname(__file__), 
        "evaluation_report.json"
    )
    
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Assertions
    for category, category_data in results.items():
        assert category_data["avg_quality_score"] > 0.5, (
            f"Category '{category}' performance is too low"
        )
        
        for query_result in category_data["queries"]:
            assert query_result["metrics"]["quality_score"] > 0.3, (
                f"Query '{query_result['query']}' performance is too low"
            )

def test_health_check():
    """
    Basic health check for the API
    """
    response = httpx.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

if __name__ == "__main__":
    pytest.main([__file__]) 