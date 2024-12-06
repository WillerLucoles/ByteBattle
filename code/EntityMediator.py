

from code.Const import WIN_HEIGHT , WIN_WIDTH , ENTITY_SPEED
from code.Entity import Entity
from code.Enemies import Enemy
import random

from code.EntityFactory import EntityFactory


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        """
        Verifica se a entidade saiu da tela.
        Se for um Enemy e sair pela esquerda, marca como 'morto'.
        """
        if isinstance(ent, Enemy) and ent.rect.right < 0:
            ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """
        Verifica se as entidades colidiram com a janela.
        """
        for entity in entity_list:
            EntityMediator.__verify_collision_window(entity)
            
    @staticmethod
    def verify_health(entity_list: list[Entity] , enemies: list[Enemy]):
        """
        Remove inimigos com health <= 0 ou que saíram da tela e cria novos inimigos.
        """
        for ent in enemies:
            if ent.health <= 0 or ent.rect.right < 0:
                print(f"[DEBUG] Removing enemy: {ent.name} (Health: {ent.health})")

                # Criar um novo tipo de inimigo aleatório
                all_enemies = EntityFactory.get_entity("Enemies")
                new_enemy = random.choice(all_enemies)

                # Configurar posição e velocidade para o novo inimigo
                new_enemy.rect.x = WIN_WIDTH
                new_enemy.rect.y = random.randint(0 , WIN_HEIGHT - new_enemy.rect.height)

                # Ajustar a velocidade com base na constante ENEMY_SPEED
                new_enemy.speed = ENTITY_SPEED.get(new_enemy.name , 3)

                # Substituir o inimigo destruído pelo novo
                enemies[enemies.index(ent)] = new_enemy

    @staticmethod
    def check_shot_collisions(shots: list , targets: list):
        """Verifica colisões entre tiros e entidades."""
        to_remove_shots = []
        for shot in shots[:]:
            for target in targets:
                if shot.rect.colliderect(target.rect):
                    #print(f"[DEBUG] Shot from {shot.name} hit {target.name}. Both shots are destroyed!")
                    to_remove_shots.append(shot)
                    target.health -= 10  # Reduz saúde da entidade atingida
                    if target.health <= 0:
                        target.health = 0
                    break

        for shot in to_remove_shots:
            shots.remove(shot)

    @staticmethod
    def check_player_enemy_collision(players: list[Entity] , enemies: list[Enemy]):
        """
        Verifica colisões entre jogadores e inimigos.
        O player perde 100 de saúde e o inimigo é reposicionado (não removido).
        Retorna True se houver colisão, indicando fim de jogo.
        """
        for player in players:
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    print(f"[DEBUG] {player.name} collided with {enemy.name}. Player loses 100 health!")
                    player.health -= 50


                    return True
        return False

