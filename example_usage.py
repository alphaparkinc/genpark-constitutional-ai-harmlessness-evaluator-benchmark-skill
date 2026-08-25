from client import ConstitutionalAiHarmlessnessEvaluatorBenchmarkClient

def main():
    client = ConstitutionalAiHarmlessnessEvaluatorBenchmarkClient()
    res = client.evaluate_model_constitutional_safety('Claude-3.7-Sonnet-Architecture')
    print('Benchmark: ' + res['benchmark_run_id'] + ' for ' + res['model_identifier'])
    print('Harmlessness: ' + str(res['harmlessness_score_pct']) + '% | Helpfulness: ' + str(res['helpfulness_score_pct']) + '%')
    print('Injection Defense Rate: ' + str(res['jailbreak_prompt_injection_defense_rate_pct']) + '% | RLAIF: ' + str(res['rl_from_ai_feedback_rlaif_converged']))

if __name__ == '__main__':
    main()
