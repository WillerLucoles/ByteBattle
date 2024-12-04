from code.Entity import Entity
from code.Enemies import Enemy


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        """Verifica se a entidade saiu da tela."""
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:  # Saiu pela esquerda
                ent.health = 0  # Marca como 'morto'

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """Verifica se as entidades colidiram com a janela ou entre si."""
        for entity in entity_list:
            EntityMediator.__verify_collision_window(entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Remove entidades com health <= 0."""
        for ent in entity_list:
            if ent.health <= 0:
                print(f"[DEBUG] Removing entity: {ent.name} (Health: {ent.health})")
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]

